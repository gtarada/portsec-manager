# -*- coding: utf-8 -*-

from dataclasses import dataclass
from ipaddress import IPv4Address
from typing import Dict

from netaddr import EUI


# TODO Add default values
@dataclass
class DHCPSnooping:
    mac_address: EUI
    ip_address: IPv4Address
    lease: int
    type: str
    vlan: int


# TODO Add default values
@dataclass
class PortSecurity:
    state: str
    maximum: int
    total: int
    sticky: int
    last_mac_address: EUI
    last_vlan: int
    violation_count: int


# TODO Add default values
# TODO Change to List
@dataclass
class MACAddressTable:
    vlan: int
    mac_address: EUI
    type: str


# TODO Add default values
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
    # dhcp_snooping: DHCPSnooping
    port_security: PortSecurity
    mac_address_table: MACAddressTable


@dataclass
class Switch:
    hostname: str
    ip_address: str
    interfaces: Dict[str, Interface]
