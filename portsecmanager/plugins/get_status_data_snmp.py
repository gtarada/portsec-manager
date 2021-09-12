# -*- coding: utf-8 -*-


import asyncio
import os
from typing import Dict

from netaddr import EUI
from nornir.core.task import Task
from portsecmanager.classes import Interface, MACAddressTable, PortSecurity, Switch
from pysnmp.hlapi.asyncio import (
    CommunityData,
    ContextData,
    ObjectIdentity,
    ObjectType,
    SnmpEngine,
    UdpTransportTarget,
    bulkCmd,
)
from pysnmp.smi import builder
from rich import print


async def async_pysnmp_bulkwalk(varBinds, host_address, snmp_community, snmp_port):
    output = {}
    snmpEngine = SnmpEngine()
    snmpBuilder = snmpEngine.getMibBuilder()
    snmpBuilder.addMibSources(builder.DirMibSource(os.path.join("mibs")))
    initialVarBinds = varBinds
    stop = False
    while True:
        (errorIndication, errorStatus, errorIndex, varBindTable) = await bulkCmd(
            snmpEngine,
            CommunityData(snmp_community),
            UdpTransportTarget((host_address, snmp_port)),
            ContextData(),
            0,
            10,
            *varBinds
        )
        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print(
                "%s at %s"
                % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
                )
            )
        else:
            for varBindRow in varBindTable:
                for idx, varBind in enumerate(varBindRow):
                    if initialVarBinds[idx][0].isPrefixOf(varBind[0]):
                        snmp_right_index = varBind[1].prettyPrint()
                        snmp_property_name = (
                            varBind[0].prettyPrint().split("::")[1].split(".")[0]
                        )
                        snmp_middle_index = (
                            varBind[0].prettyPrint().split("::")[1].split(".")[1]
                        )
                        if not output.get(snmp_middle_index):
                            output[snmp_middle_index] = {}
                        try:
                            snmp_left_index = (
                                varBind[0].prettyPrint().split("::")[1].split(".")[2]
                            )
                            if not output[snmp_middle_index].get(snmp_left_index):
                                output[snmp_middle_index][snmp_left_index] = {}
                            output[snmp_middle_index][snmp_left_index][
                                snmp_property_name
                            ] = snmp_right_index
                        except IndexError:
                            output[snmp_middle_index][
                                snmp_property_name
                            ] = snmp_right_index
                    else:
                        stop = True
        varBinds = varBindTable[-1]
        if stop:
            break
    snmpEngine.transportDispatcher.closeDispatcher()
    return output


def pysnmp_bulkwalk(snmp_bulk_objects, host_address, snmp_community, snmp_port):
    output = asyncio.run(
        async_pysnmp_bulkwalk(
            snmp_bulk_objects, host_address, snmp_community, snmp_port
        )
    )
    return output


def interface_status(admin_status: str, oper_status: str) -> str:
    if admin_status == "up" and oper_status == "up":
        return "connected"
    else:
        if admin_status == "down":
            return "disabled"
        else:
            return "unknown"


def get_interfaces_data(
    snmp_host: str, snmp_community: str, snmp_port: int
) -> Dict[str, Dict[str, str]]:
    varbinds = [
        ObjectType(ObjectIdentity("IF-MIB", "ifDescr")),
        ObjectType(ObjectIdentity("IF-MIB", "ifType")),
        ObjectType(ObjectIdentity("IF-MIB", "ifHighSpeed")),
        ObjectType(ObjectIdentity("IF-MIB", "ifAdminStatus")),
        ObjectType(ObjectIdentity("IF-MIB", "ifOperStatus")),
        ObjectType(ObjectIdentity("IF-MIB", "ifInErrors")),
        ObjectType(ObjectIdentity("IF-MIB", "ifAlias")),
    ]
    snmp_interfaces_data = pysnmp_bulkwalk(
        varbinds, snmp_host, snmp_community, snmp_port
    )
    interfaces = {}
    for ifindex in snmp_interfaces_data.keys():
        if snmp_interfaces_data[ifindex]["ifType"] == "ethernetCsmacd":
            interfaces[snmp_interfaces_data[ifindex]["ifDescr"]] = {
                "name": snmp_interfaces_data[ifindex]["ifDescr"],
                "duplex": "Unknown",
                "speed": "?",
                "vlan": "?",
                "status": interface_status(
                    snmp_interfaces_data[ifindex]["ifAdminStatus"],
                    snmp_interfaces_data[ifindex]["ifOperStatus"],
                ),
                "description": snmp_interfaces_data[ifindex]["ifAlias"],
                "errors": snmp_interfaces_data[ifindex]["ifInErrors"],
            }
    return interfaces

def get_port_security_data(snmp_host: str, snmp_community: str, snmp_port: int):
    varbinds = [
        ObjectType(ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityEnable")),
        ObjectType(ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddress")),
        ObjectType(ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddrVlanId")),
        ObjectType(ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsIfPortSecurityStatus")),
        ObjectType(ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsIfMaxSecureMacAddr")),
        ObjectType(ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsIfCurrentSecureMacAddrCount")),
        ObjectType(ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsIfViolationCount")),
    ]
    snmp_port_security_data = pysnmp_bulkwalk(
        varbinds, snmp_host, snmp_community, snmp_port
    )
    print(snmp_port_security_data)

    return None



def get_status_data_snmp(task: Task) -> Dict[str, Interface]:
    interfaces_data = get_interfaces_data(task.host.hostname, "public", 161)
    port_security = get_port_security_data(task.host.hostname, "public", 161)
    port_security = PortSecurity("?", 0, 0, 0, EUI("0000.0000.0000"), 0, 0)
    mac_address_table = MACAddressTable(0, EUI("0000.0000.0000"), "Not supported")
    interfaces = {}
    for ifname in interfaces_data.keys():
        interfaces[ifname] = Interface(
            interfaces_data[ifname]["name"],
            interfaces_data[ifname]["duplex"],
            interfaces_data[ifname]["speed"],
            interfaces_data[ifname]["vlan"],
            interfaces_data[ifname]["status"],
            interfaces_data[ifname]["description"],
            interfaces_data[ifname]["errors"],
            port_security,
            mac_address_table,
        )
    return interfaces
