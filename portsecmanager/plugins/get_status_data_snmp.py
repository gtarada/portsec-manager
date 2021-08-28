# -*- coding: utf-8 -*-


import asyncio
import os

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
    snmpBuilder.addMibSources(builder.DirMibSource(
        os.path.join('mibs')
    ))
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


def get_status_data_snmp(task: Task) -> None:
    varbinds = [
        ObjectType(ObjectIdentity("IF-MIB", "ifDescr")),
        ObjectType(ObjectIdentity("IF-MIB", "ifType")),
        ObjectType(ObjectIdentity("IF-MIB", "ifHighSpeed")),
        ObjectType(ObjectIdentity("IF-MIB", "ifAdminStatus")),
        ObjectType(ObjectIdentity("IF-MIB", "ifOperStatus")),
        ObjectType(ObjectIdentity("IF-MIB", "ifInErrors")),
        ObjectType(ObjectIdentity("IF-MIB", "ifAlias")),
    ]
    snmp_interfaces_data = pysnmp_bulkwalk(varbinds, task.host.hostname, "public", 161))

    interfaces = {}
    for ifindex in snmp_interfaces_data.keys():
        interfaces[snmp_interfaces_data[ifindex]['ifDescr']] = Interface (
                snmp_interfaces_data[ifindex]['ifDescr'],
                "-",
                snmp_interfaces_data[ifindex]['ifHighSpeed'],
                snmp_interfaces_data[ifindex]['ifType'],
                "-",
                snmp_interfaces_data[ifindex]['ifOperStatus'],
                snmp_interfaces_data[ifindex]['ifAlias'],
                snmp_interfaces_data[ifindex]['ifInErrors'],
                PortSecurity(),
                MacAddressTable(),
            )

