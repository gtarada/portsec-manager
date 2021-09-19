# -*- coding: utf-8 -*-

from typing import Dict

import click
from nornir import InitNornir
from nornir.core import Nornir
from nornir.core.filter import F
from nornir.core.inventory import Hosts

from core.plugins.console_print_switch import console_print_switch
from core.plugins.get_status_data import get_status_data

from core.plugins.clear_sticky_snmp import clear_sticky_snmp


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


def inventory_single_host(nr: Nornir, filter: str) -> Hosts:
    nr_filter_hosts = nr.filter(
        F(
            name__contains=filter,
        )
    )
    nr_hosts_list = [x for x in nr_filter_hosts.inventory.hosts.keys()]
    nr_host = nr_filter_hosts.inventory.hosts[nr_hosts_list[0]]
    return Hosts({str(nr_host): nr_host})


@click.command()
@click.option("--filter", required=True, prompt=True)
@click.option("--clear", type=str)
def main(filter: str, clear: str) -> None
    nr = InitNornir(config_file="nornir_config.yaml")
    nr.inventory.hosts = inventory_single_host(nr, filter)

    if clear:
        clear_sticky(clear, nr)
    get_status(nr)


if __name__ == "__main__":
    main()
