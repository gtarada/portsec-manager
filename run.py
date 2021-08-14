# -*- coding: utf-8 -*-

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_commands
from nornir.core.filter import F
import click


def get_report(task):
    if task.host.data["vendor"] == "cisco" and task.host.data["driver"] == "cli-ssh":
        task.host.platform = "cisco_iosxe"
        return task.run(
            send_commands,
            commands=[
                "show interfaces status | exclude routed|trunk",
                "show mac address-table secure",
            ],
        )


@click.command()
@click.option("--filter", required=True, prompt=True)
def main(filter: str):
    nr = InitNornir(config_file="nornir_config.yaml")
    hosts = nr.filter(F(name__contains=filter))
    output = hosts.run(get_report)
    print_result(output)


if __name__ == "__main__":
    main()
