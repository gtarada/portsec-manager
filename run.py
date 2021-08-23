# -*- coding: utf-8 -*-

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import click

# from web import web
from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Task
from nornir_scrapli.functions import print_structured_result
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print, box
from rich.console import Console
from rich.table import Table
from netaddr import EUI


# TODO Add default values
@dataclass
class DHCPSnooping:
    mac_address: EUI
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
    last_mac_address: EUI
    last_vlan: int
    violation_count: int


# TODO Add default values
# TODO Change to List
@dataclass
class MACAddressTable:
    vlan: int
    mac_address: EUI
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


def print_switch(switch_data: Switch) -> None:
    console = Console()

    # Print switch common data
    table = Table(show_header=True, box=box.ROUNDED)
    table.add_column("Hostname")
    table.add_column("IP address")
    table.add_row(switch_data.hostname, switch_data.ip_address)
    console.print(table)

    # Print interfaces data
    table = Table(show_header=True, box=box.SQUARE)
    table.add_column("Name", overflow="fold")
    table.add_column("Duplex")
    table.add_column("Speed")
    table.add_column("Type")
    table.add_column("VLAN")
    table.add_column("Status")
    table.add_column("Description", overflow="fold")
    table.add_column("Input errors")
    table.add_column("Port security state", overflow="fold")
    table.add_column("Port security maximum")
    table.add_column("Port security total")
    table.add_column("Port security sticky")
    table.add_column("Port security last MAC address", overflow="fold")
    table.add_column("Port security last VLAN")
    table.add_column("Port security violation count")
    for interface in switch_data.interfaces.keys():
        if switch_data.interfaces[interface].port_security.state == "Enabled":
            table.add_row(
                switch_data.interfaces[interface].name,
                switch_data.interfaces[interface].duplex,
                switch_data.interfaces[interface].speed,
                switch_data.interfaces[interface].type,
                switch_data.interfaces[interface].vlan,
                switch_data.interfaces[interface].status,
                switch_data.interfaces[interface].description,
                str(switch_data.interfaces[interface].input_errors),
                switch_data.interfaces[interface].port_security.state,
                str(switch_data.interfaces[interface].port_security.maximum),
                str(switch_data.interfaces[interface].port_security.total),
                str(switch_data.interfaces[interface].port_security.sticky),
                str(switch_data.interfaces[interface].port_security.last_mac_address)
                + " ("
                + switch_data.interfaces[interface]
                .port_security.last_mac_address.oui.registration()
                .org
                + ")",
                str(switch_data.interfaces[interface].port_security.last_vlan),
                str(switch_data.interfaces[interface].port_security.violation_count),
            )
        else:
            table.add_row(
                switch_data.interfaces[interface].name,
                switch_data.interfaces[interface].duplex,
                switch_data.interfaces[interface].speed,
                switch_data.interfaces[interface].type,
                switch_data.interfaces[interface].vlan,
                switch_data.interfaces[interface].status,
                switch_data.interfaces[interface].description,
                str(switch_data.interfaces[interface].input_errors),
                switch_data.interfaces[interface].port_security.state,
            )
    console.print(table)


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
                    EUI(portsec_struct_output["last_src_mac_addr_vlan"].split(":")[0]),
                    portsec_struct_output["last_src_mac_addr_vlan"].split(":")[1],
                    portsec_struct_output["violation_count"],
                )

                if int(portsec_struct_output["sticky_mac_addrs"]) > 0:
                    # TODO Move to another function
                    mac_command_string = (
                        f"show mac address-table interface {interface_name}"
                    )
                    mac_nr_task_result = task.run(
                        send_command, command=mac_command_string
                    )
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
                        EUI("0000.0000.0000"),
                        "None",
                    )

            else:
                port_security = PortSecurity(
                    "Not supported", 0, 0, 0, EUI("0000.0000.0000"), 0, 0
                )
                mac_address_table = MACAddressTable(
                    0, EUI("0000.0000.0000"), "Not supported"
                )

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
                mac_address_table,
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
        print_switch(switches[switch])
    # print(switches)


if __name__ == "__main__":
    main()
