# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import click
from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Task
from nornir_scrapli.functions import print_structured_result
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print

# TODO Add default values
@dataclass
class DHCPSnooping:
    mac_address: str
    ip_address: str
    lease: int
    type: str
    vlan: int

# TODO Add default values
@dataclass
class PortSecurity:
    state: str
    maximum: int
    total: int
    sticky: int
    last_mac_address: str
    last_vlan: int
    violation_count: int

# TODO Add default values
# TODO Change to List
@dataclass
class MACAddressTable:
    vlan: int
    mac_address: str
    type: str

# TODO Add default values
@dataclass
class Interface:
    name: str
    duplex: str
    speed: str
    type: str
    vlan: str
    status: str
    description: str
    input_errors: int
    # dhcp_snooping: DHCPSnooping
    port_security: PortSecurity
    mac_address_table: MACAddressTable


@dataclass
class Switch:
    hostname: str
    ip_address: str
    interfaces: Dict[str, Interface]


# TODO
def short_name(name: str) -> Optional[str]:
    regex = "^([a-zA-Z]+)(\d+\/\d+)$"
    return None


# TODO Move to plugins
def get_status_data(task: Task) -> Switch:
    if task.host.data["vendor"] == "cisco" and task.host.data["driver"] == "cli-ssh":
        task.host.platform = "cisco_iosxe"
        # Get interfaces status data
        # TODO Move to another function
        command_string = "show interfaces status"
        nr_task_result = task.run(send_command, command=command_string)
        struct_output = nr_task_result[0].scrapli_response.genie_parse_output()
        interfaces = {}
        for interface_name in struct_output["interfaces"].keys():
            # Check for blank description
            if "name" not in struct_output["interfaces"][interface_name]:
                struct_output["interfaces"][interface_name]["name"] = ""
            # Get interface detail data
            # TODO Move to another function
            int_command_string = f"show interface {interface_name}"
            int_nr_task_result = task.run(send_command, command=int_command_string)
            int_struct_output = int_nr_task_result[
                0
            ].scrapli_response.genie_parse_output()

            # TODO Move to another function
            # TODO Add custom TextFSM template
            # ipdhcp_command_string = f"show ip dhcp snooping binding interface {interface_name}"
            # ipdhcp_nr_task_result = task.run(send_command, command=ipdhcp_command_string)
            # ipdhcp_struct_output = ipdhcp_nr_task_result[
            #     0
            # ].scrapli_response.textfsm_parse_output()
            # print(ipdhcp_struct_output)

            if struct_output["interfaces"][interface_name]["vlan"] != "routed":

                # TODO Move to another function
                portsec_command_string = (
                    f"show port-security interface {interface_name}"
                )
                portsec_nr_task_result = task.run(
                    send_command, command=portsec_command_string
                )
                portsec_struct_output = portsec_nr_task_result[
                    0
                ].scrapli_response.textfsm_parse_output()[0]
                port_security = PortSecurity(
                    portsec_struct_output["port_security"],
                    portsec_struct_output["max_mac_addrs"],
                    portsec_struct_output["total_mac_addrs"],
                    portsec_struct_output["sticky_mac_addrs"],
                    portsec_struct_output["last_src_mac_addr_vlan"].split(":")[0],
                    portsec_struct_output["last_src_mac_addr_vlan"].split(":")[1],
                    portsec_struct_output["violation_count"],
                )

                if int(portsec_struct_output["sticky_mac_addrs"]) > 0:
                    # TODO Move to another function
                    mac_command_string = (
                        f"show mac address-table interface {interface_name}"
                    )
                    mac_nr_task_result = task.run(send_command, command=mac_command_string)
                    mac_struct_output = mac_nr_task_result[
                        0
                    ].scrapli_response.textfsm_parse_output()[0]
                    mac_address_table = MACAddressTable(
                        mac_struct_output["vlan"],
                        mac_struct_output["destination_address"],
                        mac_struct_output["type"],
                    )
                else:
                    mac_address_table = MACAddressTable(
                        0,
                        '0000.0000.0000',
                        'None',
                    )

            else:
                port_security = PortSecurity(
                    "Not supported", 0, 0, 0, "0000.0000.0000", 0, 0
                )
                mac_address_table = MACAddressTable(0, "0000.0000.0000", 'Not supported')

            # Fill interfaces list
            interfaces[interface_name] = Interface(
                interface_name,
                struct_output["interfaces"][interface_name]["duplex_code"],
                struct_output["interfaces"][interface_name]["port_speed"],
                struct_output["interfaces"][interface_name]["type"],
                struct_output["interfaces"][interface_name]["vlan"],
                struct_output["interfaces"][interface_name]["status"],
                struct_output["interfaces"][interface_name]["name"],
                int_struct_output[interface_name]["counters"]["in_errors"],
                port_security,
                mac_address_table
            )
    return Switch(task.host.name, task.host.hostname, interfaces)


@click.command()
@click.option("--filter", required=True, prompt=True)
def main(filter: str):
    nr = InitNornir(config_file="nornir_config.yaml")
    hosts = nr.filter(F(name__contains=filter))
    output = hosts.run(get_status_data)
    switches = {}
    for switch in output.keys():
        switches[switch] = output[switch].result
    print(switches)


if __name__ == "__main__":
    main()
