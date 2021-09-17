# -*- coding: utf-8 -*-

import click
from nornir import InitNornir
from nornir.core.filter import F

from core.plugins.get_status_data import get_status_data
from core.plugins.console_print_switch import console_print_switch


def get_status(filter: str) -> None:
    nr = InitNornir(config_file="nornir_config.yaml")
    hosts = nr.filter(F(name__contains=filter))
    # TODO add progressbar
    output = hosts.run(get_status_data)
    switches = {}
    for switch in output.keys():
        switches[switch] = output[switch].result
        console_print_switch(switches[switch])


def clear_sticky(clear: str) -> None:
    pass


@click.command()
@click.option("--filter", required=True, prompt=True)
@click.option("--clear", type=str)
def main(filter: str, clear: str) -> None:
    if clear:
        clear_sticky(clear)
    else:
        get_status(filter)


if __name__ == "__main__":
    main()
