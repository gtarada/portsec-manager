# -*- coding: utf-8 -*-

from core.classes import Switch
from tabulate import tabulate
from pprint import pp


def print_switch_web(switch_data: Switch) -> None:
    output = tabulate(
        [{"Hostname": switch_data.hostname, "IP address": str(switch_data.ip_address)}],
        headers="keys",
        tablefmt="html",
    )
    table = []
    for interface in switch_data.interfaces.keys():
        if switch_data.interfaces[interface].port_security.state == "Enabled":
            table.append(
                {
                    "Name": switch_data.interfaces[interface].name,
                    "Duplex": switch_data.interfaces[interface].duplex,
                    "Speed": switch_data.interfaces[interface].speed,
                    "VLAN": switch_data.interfaces[interface].vlan,
                    "Status": switch_data.interfaces[interface].status,
                    "Description": switch_data.interfaces[interface].description,
                    "Input errors": str(switch_data.interfaces[interface].input_errors),
                    "Port security maximum": str(
                        switch_data.interfaces[interface].port_security.maximum
                    ),
                    "Port security sticky": str(
                        switch_data.interfaces[interface].port_security.sticky
                    ),
                    "Port security last MAC address": str(
                        switch_data.interfaces[interface].port_security.last_mac_address
                    ),
                    "Port security violation count": str(
                        switch_data.interfaces[interface].port_security.violation_count
                    ),
                    "Port security secure MAC address": " ".join(
                        str(x)
                        for x in switch_data.interfaces[
                            interface
                        ].port_security.secure_mac_addresses
                    ),
                }
            )
        else:
            table.append(
                {
                    "Name": switch_data.interfaces[interface].name,
                    "Duplex": switch_data.interfaces[interface].duplex,
                    "Speed": switch_data.interfaces[interface].speed,
                    "VLAN": switch_data.interfaces[interface].vlan,
                    "Status": switch_data.interfaces[interface].status,
                    "Description": switch_data.interfaces[interface].description,
                    "Input errors": str(switch_data.interfaces[interface].input_errors),
                }
            )
    output += tabulate(table, headers="keys", tablefmt="html")
    return output
