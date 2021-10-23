# -*- coding: utf-8 -*-

from typing import Dict

import click
from nornir import InitNornir
from nornir.core import Nornir

from core.plugins.clear_sticky_snmp import clear_sticky_snmp
from core.plugins.console_print_switch import console_print_switch
from core.plugins.get_status_data import get_status_data
from core.plugins.inv.single_host import single_host


def get_status(nr: Nornir) -> None:
    # TODO add progressbar
    output = nr.run(get_status_data)
    switches = {}
    for switch in output.keys():
        switches[switch] = output[switch].result
        console_print_switch(switches[switch])


def clear_sticky(clear: str, nr: Nornir) -> None:
    # TODO Interface or MAC address check
    iface = clear
    # TODO Check device properties and model
    output = nr.run(clear_sticky_snmp, iface=clear)

@click.command()
@click.option("--filter", required=True, prompt=True)
@click.option("--clear", type=str)
def main(filter: str, clear: str) -> None:
    nr = InitNornir(config_file="nornir_config.yaml")
    nr.inventory.hosts = single_host(nr, filter)

    if clear:
        clear_sticky(clear, nr)
    get_status(nr)


if __name__ == "__main__":
    main()
