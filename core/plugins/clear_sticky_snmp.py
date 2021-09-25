# -*- coding: utf-8 -*-

from nornir.core.task import Task
from netaddr import EUI, mac_unix
from pysnmp.hlapi import (
    setCmd,
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    getCmd,
    nextCmd,
)
from pysnmp.smi import builder
import os


def snmpset_clear_iface(hostname: str, community: str, ifindex: int) -> None:
    snmpEngine = SnmpEngine()
    snmpBuilder = snmpEngine.getMibBuilder()
    snmpBuilder.addMibSources(builder.DirMibSource(os.path.join("mibs")))
    g = setCmd(
        snmpEngine,
        CommunityData(community),
        UdpTransportTarget((hostname, 161)),
        ContextData(),
        ObjectType(
            ObjectIdentity(
                # "CISCO-PORT-SECURITY-MIB", "cpsIfClearSecureMacAddresses", ifindex
                "CISCO-PORT-SECURITY-MIB",
                "cpsIfClearSecureAddresses",
                ifindex,
            ),
            1,
        ),
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            "%s at %s"
            % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
            )
        )
    else:
        for varBind in varBinds:
            print(" = ".join([x.prettyPrint() for x in varBind]))


def snmpget_last_mac_address(hostname: str, community: str, ifindex: int) -> EUI:
    snmpEngine = SnmpEngine()
    snmpBuilder = snmpEngine.getMibBuilder()
    snmpBuilder.addMibSources(builder.DirMibSource(os.path.join("mibs")))
    g = getCmd(
        snmpEngine,
        CommunityData(community),
        UdpTransportTarget((hostname, 161)),
        ContextData(),
        ObjectType(
            ObjectIdentity(
                "CISCO-PORT-SECURITY-MIB", "cpsIfSecureLastMacAddress", ifindex
            )
        ),
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            "%s at %s"
            % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
            )
        )
    else:
        for varBind in varBinds:
            output = [x.prettyPrint() for x in varBind][1]
    return EUI(output, version=48, dialect=mac_unix)


def snmpget_secure_mac_address(hostname: str, community: str, ifindex: int) -> EUI:
    snmpEngine = SnmpEngine()
    snmpBuilder = snmpEngine.getMibBuilder()
    snmpBuilder.addMibSources(builder.DirMibSource(os.path.join("mibs")))
    g = nextCmd(
        snmpEngine,
        CommunityData(community),
        UdpTransportTarget((hostname, 161)),
        ContextData(),
        ObjectType(
            ObjectIdentity("CISCO-PORT-SECURITY-MIB", "cpsSecureMacAddrType", ifindex)
        ),
    )
    output = []
    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            "%s at %s"
            % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
            )
        )
    else:
        for varBind in varBinds:
            right_value = [x.prettyPrint() for x in varBind][0]
            address = right_value[right_value.find('"') + 1 : len(right_value) - 1]
            output.append(EUI(address, version=48, dialect=mac_unix))
    return output


def clear_sticky_snmp(task: Task, iface: str) -> None:
    ifindex = 2
    last_mac = snmpget_last_mac_address(
        task.host.hostname, task.host.data["community"], ifindex
    )
    secure_macs = snmpget_secure_mac_address(
        task.host.hostname, task.host.data["community"], ifindex
    )
    found = False
    # FIXME check if clear secure mac from old interface (notconnect?)
    # for secure_mac in secure_macs:
    #     if last_mac == secure_mac:
    #         found = True
    # if not found:
    snmpset_clear_iface(task.host.hostname, task.host.data["community_rw"], ifindex)
