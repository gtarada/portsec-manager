# -*- coding: utf-8 -*-

from nornir.core import Nornir
from nornir.core.filter import F
from nornir.core.inventory import Hosts


def single_host(nr: Nornir, filter: str) -> Hosts:
    nr_filter_hosts = nr.filter(
        F(
            name__contains=filter,
        )
    )
    nr_hosts_list = [x for x in nr_filter_hosts.inventory.hosts.keys()]
    nr_host = nr_filter_hosts.inventory.hosts[nr_hosts_list[0]]
    return Hosts({str(nr_host): nr_host})
