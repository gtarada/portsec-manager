# -*- coding: utf-8 -*-

import click
from nornir import InitNornir
from nornir.core.filter import F

from portsecmanager.plugins.get_status_data_cli_ssh import get_status_data
from portsecmanager.plugins.console_print_switch import console_print_switch


@click.command()
@click.option("--filter", required=True, prompt=True)
def main(filter: str) -> None:
    nr = InitNornir(config_file="nornir_config.yaml")
    hosts = nr.filter(F(name__contains=filter))
    output = hosts.run(get_status_data)
    switches = {}
    for switch in output.keys():
        switches[switch] = output[switch].result
        console_print_switch(switches[switch])

if __name__ == "__main__":
    main()
