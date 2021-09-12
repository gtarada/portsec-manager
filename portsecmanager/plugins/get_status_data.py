# -*- coding: utf-8 -*-

from ipaddress import IPv4Address

from netaddr import EUI
from nornir.core.task import Task
from nornir_scrapli.tasks import send_command
from portsecmanager.classes import Interface, MACAddressTable, PortSecurity, Switch
from portsecmanager.plugins.get_status_data_snmp import get_status_data_snmp


# TODO add progressbar
def get_status_data(task: Task) -> Switch:
    interfaces = {}
    # TODO Move to plugins
    if task.host.data["vendor"] == "cisco" and task.host.data["driver"] == "cli-ssh":
        task.host.platform = "cisco_iosxe"
        # Get interfaces status data
        # TODO Move to another function
        command_string = "show interfaces status"
        nr_task_result = task.run(send_command, command=command_string)
        struct_output = nr_task_result[0].scrapli_response.textfsm_parse_output()
        for interface_data in struct_output:
            # Get interface detail data
            # TODO Move to another function
            int_command_string = f"show interface {interface_data['port']}"
            int_nr_task_result = task.run(send_command, command=int_command_string)
            int_struct_output = int_nr_task_result[
                0
            ].scrapli_response.textfsm_parse_output()

            # TODO Move to another function
            # TODO Add custom TextFSM template
            # ipdhcp_command_string = f"show ip dhcp snooping binding interface {interface_name}"
            # ipdhcp_nr_task_result = task.run(send_command, command=ipdhcp_command_string)
            # ipdhcp_struct_output = ipdhcp_nr_task_result[
            #     0
            # ].scrapli_response.textfsm_parse_output()
            # print(ipdhcp_struct_output)

            if interface_data["vlan"] != "routed":

                # TODO Move to another function
                portsec_command_string = (
                    f"show port-security interface {interface_data['port']}"
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
                        f"show mac address-table interface {interface_data['port']}"
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
            interfaces[interface_data["port"]] = Interface(
                interface_data["port"],
                interface_data["duplex"],
                interface_data["speed"],
                interface_data["vlan"],
                interface_data["status"],
                interface_data["name"],
                int_struct_output[0]["input_errors"],
                port_security,
                mac_address_table,
            )

    if task.host.data["vendor"] == "cisco" and task.host.data["driver"] == "snmp":
        # Get data with SNMP
        interfaces = get_status_data_snmp(task)

    return Switch(task.host.name, IPv4Address(task.host.hostname), interfaces)
