# -*- coding: utf-8 -*-

from core.classes import Switch
from rich import box, print
from rich.console import Console
from rich.table import Table


def console_print_switch(switch_data: Switch) -> None:
    console = Console()

    # Print switch common data
    table = Table(show_header=True, box=box.ROUNDED)
    table.add_column("Hostname")
    table.add_column("IP address")
    table.add_row(switch_data.hostname, str(switch_data.ip_address))
    console.print(table)

    # Print interfaces data
    table = Table(show_header=True, box=box.SQUARE)
    table.add_column("Name", overflow="fold")
    table.add_column("Duplex")
    table.add_column("Speed")
    table.add_column("VLAN")
    table.add_column("Status")
    table.add_column("Description", overflow="fold")
    table.add_column("Input errors")
    table.add_column("Port security state", overflow="fold")
    table.add_column("Port security maximum")
    table.add_column("Port security sticky")
    table.add_column("Port security last MAC address", overflow="fold")
    table.add_column("Port security violation count")
    table.add_column("Port security secure MAC address", overflow="fold")
    for interface in switch_data.interfaces.keys():
        if switch_data.interfaces[interface].port_security.state == "Enabled":
            table.add_row(
                switch_data.interfaces[interface].name,
                switch_data.interfaces[interface].duplex,
                switch_data.interfaces[interface].speed,
                switch_data.interfaces[interface].vlan,
                switch_data.interfaces[interface].status,
                switch_data.interfaces[interface].description,
                str(switch_data.interfaces[interface].input_errors),
                switch_data.interfaces[interface].port_security.state,
                str(switch_data.interfaces[interface].port_security.maximum),
                str(switch_data.interfaces[interface].port_security.sticky),
                str(switch_data.interfaces[interface].port_security.last_mac_address),
                str(switch_data.interfaces[interface].port_security.violation_count),
                " ".join(
                    str(x)
                    for x in switch_data.interfaces[
                        interface
                    ].port_security.secure_mac_addresses
                ),
            )
        else:
            table.add_row(
                switch_data.interfaces[interface].name,
                switch_data.interfaces[interface].duplex,
                switch_data.interfaces[interface].speed,
                switch_data.interfaces[interface].vlan,
                switch_data.interfaces[interface].status,
                switch_data.interfaces[interface].description,
                str(switch_data.interfaces[interface].input_errors),
                switch_data.interfaces[interface].port_security.state,
            )
    console.print(table)
