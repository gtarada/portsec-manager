# -*- coding: utf-8 -*-

from dataclasses import dataclass, field

import click
from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Task
from nornir_scrapli.tasks import send_command
from nornir_scrapli.functions import print_structured_result
from nornir_utils.plugins.functions import print_result
from typing import List
from rich import print


# @dataclass
# class DHCPSnooping:

# @dataclass
# class PortSecurity:


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


#     dhcp_snooping: DHCPSnooping
#     port_security: PortSecurity


@dataclass
class Switch:
    hostname: str
    ip_address: str
    interfaces: List[Interface]


# TODO Move to plugins
def get_status_data(task: Task) -> Switch:
    if task.host.data["vendor"] == "cisco" and task.host.data["driver"] == "cli-ssh":
        task.host.platform = "cisco_iosxe"
        # Get interfaces status data
        # TODO Move to another function
        command_string = "show interfaces status"
        nr_task_result = task.run(send_command, command=command_string)
        struct_output = nr_task_result[0].scrapli_response.genie_parse_output()
        interfaces = []
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
            # Fill interfaces list
            interfaces.append(
                Interface(
                    interface_name,
                    struct_output["interfaces"][interface_name]["duplex_code"],
                    struct_output["interfaces"][interface_name]["port_speed"],
                    struct_output["interfaces"][interface_name]["type"],
                    struct_output["interfaces"][interface_name]["vlan"],
                    struct_output["interfaces"][interface_name]["status"],
                    struct_output["interfaces"][interface_name]["name"],
                    int_struct_output[interface_name]["counters"]["in_errors"],
                )
            )
    return Switch(task.host.name, task.host.hostname, interfaces)


@click.command()
@click.option("--filter", required=True, prompt=True)
def main(filter: str):
    nr = InitNornir(config_file="nornir_config.yaml")
    hosts = nr.filter(F(name__contains=filter))
    output = hosts.run(get_status_data)
    switches = []
    for switch in output.keys():
        switches.append(output[switch].result)
    print(switches)


if __name__ == "__main__":
    main()
