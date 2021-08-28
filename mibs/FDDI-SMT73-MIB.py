#
# PySNMP MIB module FDDI-SMT73-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://www.circitor.fr:80/Mibs/Mib/F/FDDI-SMT73-MIB.mib
# Produced by pysmi-0.3.4 at Sat Aug 28 16:40:29 2021
# On host thinkpad platform Linux version 4.4.0-19041-Microsoft by user gtarada
# Using Python version 3.9.5 (default, May 19 2021, 11:32:47) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, MibIdentifier, TimeTicks, ModuleIdentity, iso, transmission, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ObjectIdentity, Bits, IpAddress, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "iso", "transmission", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits", "IpAddress", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fddi = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15))
fddimib = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73))
class FddiTimeNano(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FddiTimeMilli(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FddiResourceId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class FddiSMTStationIdType(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class FddiMACLongAddressType(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

fddimibSMT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 1))
fddimibMAC = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 2))
fddimibMACCounters = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 3))
fddimibPATH = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 4))
fddimibPORT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 15, 73, 5))
fddimibSMTNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTNumber.setStatus('mandatory')
fddimibSMTTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2), )
if mibBuilder.loadTexts: fddimibSMTTable.setStatus('mandatory')
fddimibSMTEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1), ).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibSMTIndex"))
if mibBuilder.loadTexts: fddimibSMTEntry.setStatus('mandatory')
fddimibSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTIndex.setStatus('mandatory')
fddimibSMTStationId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 2), FddiSMTStationIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTStationId.setStatus('mandatory')
fddimibSMTOpVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTOpVersionId.setStatus('mandatory')
fddimibSMTHiVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTHiVersionId.setStatus('mandatory')
fddimibSMTLoVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTLoVersionId.setStatus('mandatory')
fddimibSMTUserData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibSMTUserData.setStatus('mandatory')
fddimibSMTMIBVersionId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTMIBVersionId.setStatus('mandatory')
fddimibSMTMACCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTMACCts.setStatus('mandatory')
fddimibSMTNonMasterCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTNonMasterCts.setStatus('mandatory')
fddimibSMTMasterCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTMasterCts.setStatus('mandatory')
fddimibSMTAvailablePaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTAvailablePaths.setStatus('mandatory')
fddimibSMTConfigCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTConfigCapabilities.setStatus('mandatory')
fddimibSMTConfigPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibSMTConfigPolicy.setStatus('mandatory')
fddimibSMTConnectionPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32768, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibSMTConnectionPolicy.setStatus('mandatory')
fddimibSMTTNotify = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibSMTTNotify.setStatus('mandatory')
fddimibSMTStatRptPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibSMTStatRptPolicy.setStatus('mandatory')
fddimibSMTTraceMaxExpiration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 17), FddiTimeMilli()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibSMTTraceMaxExpiration.setStatus('mandatory')
fddimibSMTBypassPresent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTBypassPresent.setStatus('mandatory')
fddimibSMTECMState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ec0", 1), ("ec1", 2), ("ec2", 3), ("ec3", 4), ("ec4", 5), ("ec5", 6), ("ec6", 7), ("ec7", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTECMState.setStatus('mandatory')
fddimibSMTCFState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("cf0", 1), ("cf1", 2), ("cf2", 3), ("cf3", 4), ("cf4", 5), ("cf5", 6), ("cf6", 7), ("cf7", 8), ("cf8", 9), ("cf9", 10), ("cf10", 11), ("cf11", 12), ("cf12", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTCFState.setStatus('mandatory')
fddimibSMTRemoteDisconnectFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTRemoteDisconnectFlag.setStatus('mandatory')
fddimibSMTStationStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("concatenated", 1), ("separated", 2), ("thru", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTStationStatus.setStatus('mandatory')
fddimibSMTPeerWrapFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTPeerWrapFlag.setStatus('mandatory')
fddimibSMTTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 24), FddiTimeMilli()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTTimeStamp.setStatus('mandatory')
fddimibSMTTransitionTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 25), FddiTimeMilli()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibSMTTransitionTimeStamp.setStatus('mandatory')
fddimibSMTStationAction = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 1, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("connect", 2), ("disconnect", 3), ("path-Test", 4), ("self-Test", 5), ("disable-a", 6), ("disable-b", 7), ("disable-m", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibSMTStationAction.setStatus('mandatory')
fddimibMACNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACNumber.setStatus('mandatory')
fddimibMACTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2), )
if mibBuilder.loadTexts: fddimibMACTable.setStatus('mandatory')
fddimibMACEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1), ).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibMACSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibMACIndex"))
if mibBuilder.loadTexts: fddimibMACEntry.setStatus('mandatory')
fddimibMACSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACSMTIndex.setStatus('mandatory')
fddimibMACIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACIndex.setStatus('mandatory')
fddimibMACIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACIfIndex.setStatus('mandatory')
fddimibMACFrameStatusFunctions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACFrameStatusFunctions.setStatus('mandatory')
fddimibMACTMaxCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 5), FddiTimeNano()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTMaxCapability.setStatus('mandatory')
fddimibMACTVXCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 6), FddiTimeNano()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTVXCapability.setStatus('mandatory')
fddimibMACAvailablePaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACAvailablePaths.setStatus('mandatory')
fddimibMACCurrentPath = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("isolated", 1), ("local", 2), ("secondary", 3), ("primary", 4), ("concatenated", 5), ("thru", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACCurrentPath.setStatus('mandatory')
fddimibMACUpstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 9), FddiMACLongAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACUpstreamNbr.setStatus('mandatory')
fddimibMACDownstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 10), FddiMACLongAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACDownstreamNbr.setStatus('mandatory')
fddimibMACOldUpstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 11), FddiMACLongAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACOldUpstreamNbr.setStatus('mandatory')
fddimibMACOldDownstreamNbr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 12), FddiMACLongAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACOldDownstreamNbr.setStatus('mandatory')
fddimibMACDupAddressTest = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("pass", 2), ("fail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACDupAddressTest.setStatus('mandatory')
fddimibMACRequestedPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibMACRequestedPaths.setStatus('mandatory')
fddimibMACDownstreamPORTType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("a", 1), ("b", 2), ("s", 3), ("m", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACDownstreamPORTType.setStatus('mandatory')
fddimibMACSMTAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 16), FddiMACLongAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACSMTAddress.setStatus('mandatory')
fddimibMACTReq = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 17), FddiTimeNano()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTReq.setStatus('mandatory')
fddimibMACTNeg = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 18), FddiTimeNano()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTNeg.setStatus('mandatory')
fddimibMACTMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 19), FddiTimeNano()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTMax.setStatus('mandatory')
fddimibMACTvxValue = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 20), FddiTimeNano()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTvxValue.setStatus('mandatory')
fddimibMACFrameCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACFrameCts.setStatus('mandatory')
fddimibMACCopiedCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACCopiedCts.setStatus('mandatory')
fddimibMACTransmitCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTransmitCts.setStatus('mandatory')
fddimibMACErrorCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACErrorCts.setStatus('mandatory')
fddimibMACLostCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACLostCts.setStatus('mandatory')
fddimibMACFrameErrorThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibMACFrameErrorThreshold.setStatus('mandatory')
fddimibMACFrameErrorRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACFrameErrorRatio.setStatus('mandatory')
fddimibMACRMTState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("rm0", 1), ("rm1", 2), ("rm2", 3), ("rm3", 4), ("rm4", 5), ("rm5", 6), ("rm6", 7), ("rm7", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACRMTState.setStatus('mandatory')
fddimibMACDaFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACDaFlag.setStatus('mandatory')
fddimibMACUnaDaFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACUnaDaFlag.setStatus('mandatory')
fddimibMACFrameErrorFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACFrameErrorFlag.setStatus('mandatory')
fddimibMACMAUnitdataAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACMAUnitdataAvailable.setStatus('mandatory')
fddimibMACHardwarePresent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACHardwarePresent.setStatus('mandatory')
fddimibMACMAUnitdataEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 2, 2, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibMACMAUnitdataEnable.setStatus('mandatory')
fddimibMACCountersTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1), )
if mibBuilder.loadTexts: fddimibMACCountersTable.setStatus('mandatory')
fddimibMACCountersEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1), ).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibMACSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibMACIndex"))
if mibBuilder.loadTexts: fddimibMACCountersEntry.setStatus('mandatory')
fddimibMACTokenCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTokenCts.setStatus('mandatory')
fddimibMACTvxExpiredCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACTvxExpiredCts.setStatus('mandatory')
fddimibMACNotCopiedCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACNotCopiedCts.setStatus('mandatory')
fddimibMACLateCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACLateCts.setStatus('mandatory')
fddimibMACRingOpCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACRingOpCts.setStatus('mandatory')
fddimibMACNotCopiedRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACNotCopiedRatio.setStatus('mandatory')
fddimibMACNotCopiedFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibMACNotCopiedFlag.setStatus('mandatory')
fddimibMACNotCopiedThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibMACNotCopiedThreshold.setStatus('mandatory')
fddimibPATHNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHNumber.setStatus('mandatory')
fddimibPATHTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2), )
if mibBuilder.loadTexts: fddimibPATHTable.setStatus('mandatory')
fddimibPATHEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1), ).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibPATHSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibPATHIndex"))
if mibBuilder.loadTexts: fddimibPATHEntry.setStatus('mandatory')
fddimibPATHSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHSMTIndex.setStatus('mandatory')
fddimibPATHIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHIndex.setStatus('mandatory')
fddimibPATHTVXLowerBound = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 3), FddiTimeNano()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPATHTVXLowerBound.setStatus('mandatory')
fddimibPATHTMaxLowerBound = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 4), FddiTimeNano()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPATHTMaxLowerBound.setStatus('mandatory')
fddimibPATHMaxTReq = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 2, 1, 5), FddiTimeNano()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPATHMaxTReq.setStatus('mandatory')
fddimibPATHConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3), )
if mibBuilder.loadTexts: fddimibPATHConfigTable.setStatus('mandatory')
fddimibPATHConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1), ).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibPATHConfigSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibPATHConfigPATHIndex"), (0, "FDDI-SMT73-MIB", "fddimibPATHConfigTokenOrder"))
if mibBuilder.loadTexts: fddimibPATHConfigEntry.setStatus('mandatory')
fddimibPATHConfigSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHConfigSMTIndex.setStatus('mandatory')
fddimibPATHConfigPATHIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHConfigPATHIndex.setStatus('mandatory')
fddimibPATHConfigTokenOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHConfigTokenOrder.setStatus('mandatory')
fddimibPATHConfigResourceType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("mac", 2), ("port", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHConfigResourceType.setStatus('mandatory')
fddimibPATHConfigResourceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHConfigResourceIndex.setStatus('mandatory')
fddimibPATHConfigCurrentPath = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("isolated", 1), ("local", 2), ("secondary", 3), ("primary", 4), ("concatenated", 5), ("thru", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPATHConfigCurrentPath.setStatus('mandatory')
fddimibPORTNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTNumber.setStatus('mandatory')
fddimibPORTTable = MibTable((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2), )
if mibBuilder.loadTexts: fddimibPORTTable.setStatus('mandatory')
fddimibPORTEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1), ).setIndexNames((0, "FDDI-SMT73-MIB", "fddimibPORTSMTIndex"), (0, "FDDI-SMT73-MIB", "fddimibPORTIndex"))
if mibBuilder.loadTexts: fddimibPORTEntry.setStatus('mandatory')
fddimibPORTSMTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTSMTIndex.setStatus('mandatory')
fddimibPORTIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTIndex.setStatus('mandatory')
fddimibPORTMyType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("a", 1), ("b", 2), ("s", 3), ("m", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTMyType.setStatus('mandatory')
fddimibPORTNeighborType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("a", 1), ("b", 2), ("s", 3), ("m", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTNeighborType.setStatus('mandatory')
fddimibPORTConnectionPolicies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPORTConnectionPolicies.setStatus('mandatory')
fddimibPORTMACIndicated = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tVal9FalseRVal9False", 1), ("tVal9FalseRVal9True", 2), ("tVal9TrueRVal9False", 3), ("tVal9TrueRVal9True", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTMACIndicated.setStatus('mandatory')
fddimibPORTCurrentPath = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ce0", 1), ("ce1", 2), ("ce2", 3), ("ce3", 4), ("ce4", 5), ("ce5", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTCurrentPath.setStatus('mandatory')
fddimibPORTRequestedPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPORTRequestedPaths.setStatus('mandatory')
fddimibPORTMACPlacement = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 9), FddiResourceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTMACPlacement.setStatus('mandatory')
fddimibPORTAvailablePaths = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTAvailablePaths.setStatus('mandatory')
fddimibPORTPMDClass = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("multimode", 1), ("single-mode1", 2), ("single-mode2", 3), ("sonet", 4), ("low-cost-fiber", 5), ("twisted-pair", 6), ("unknown", 7), ("unspecified", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTPMDClass.setStatus('mandatory')
fddimibPORTConnectionCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTConnectionCapabilities.setStatus('mandatory')
fddimibPORTBSFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTBSFlag.setStatus('mandatory')
fddimibPORTLCTFailCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTLCTFailCts.setStatus('mandatory')
fddimibPORTLerEstimate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTLerEstimate.setStatus('mandatory')
fddimibPORTLemRejectCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTLemRejectCts.setStatus('mandatory')
fddimibPORTLemCts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTLemCts.setStatus('mandatory')
fddimibPORTLerCutoff = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPORTLerCutoff.setStatus('mandatory')
fddimibPORTLerAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPORTLerAlarm.setStatus('mandatory')
fddimibPORTConnectState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("connecting", 2), ("standby", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTConnectState.setStatus('mandatory')
fddimibPORTPCMState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("pc0", 1), ("pc1", 2), ("pc2", 3), ("pc3", 4), ("pc4", 5), ("pc5", 6), ("pc6", 7), ("pc7", 8), ("pc8", 9), ("pc9", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTPCMState.setStatus('mandatory')
fddimibPORTPCWithhold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("m-m", 2), ("otherincompatible", 3), ("pathnotavailable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTPCWithhold.setStatus('mandatory')
fddimibPORTLerFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTLerFlag.setStatus('mandatory')
fddimibPORTHardwarePresent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fddimibPORTHardwarePresent.setStatus('mandatory')
fddimibPORTAction = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 15, 73, 5, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("maintPORT", 2), ("enablePORT", 3), ("disablePORT", 4), ("startPORT", 5), ("stopPORT", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fddimibPORTAction.setStatus('mandatory')
mibBuilder.exportSymbols("FDDI-SMT73-MIB", fddimibMACTransmitCts=fddimibMACTransmitCts, fddimibMACMAUnitdataAvailable=fddimibMACMAUnitdataAvailable, fddimibMACFrameErrorRatio=fddimibMACFrameErrorRatio, fddimibMACNotCopiedRatio=fddimibMACNotCopiedRatio, fddimibPORTLemRejectCts=fddimibPORTLemRejectCts, FddiSMTStationIdType=FddiSMTStationIdType, fddimibMACOldDownstreamNbr=fddimibMACOldDownstreamNbr, fddimibMACTokenCts=fddimibMACTokenCts, fddimibMACNotCopiedThreshold=fddimibMACNotCopiedThreshold, fddimibMACMAUnitdataEnable=fddimibMACMAUnitdataEnable, fddimibPORTLemCts=fddimibPORTLemCts, fddimibMACAvailablePaths=fddimibMACAvailablePaths, fddimibMACCurrentPath=fddimibMACCurrentPath, fddimibSMTLoVersionId=fddimibSMTLoVersionId, fddimibSMTCFState=fddimibSMTCFState, fddimibPORTLerEstimate=fddimibPORTLerEstimate, fddimibPORTAction=fddimibPORTAction, fddimibMACSMTAddress=fddimibMACSMTAddress, fddimibPORTPCWithhold=fddimibPORTPCWithhold, fddimibPATH=fddimibPATH, fddimibPORTRequestedPaths=fddimibPORTRequestedPaths, fddimibMACNotCopiedFlag=fddimibMACNotCopiedFlag, fddimibMACSMTIndex=fddimibMACSMTIndex, fddimibSMTHiVersionId=fddimibSMTHiVersionId, fddimibMACFrameCts=fddimibMACFrameCts, fddimibSMTECMState=fddimibSMTECMState, fddimibMACTMaxCapability=fddimibMACTMaxCapability, fddimibPORTPCMState=fddimibPORTPCMState, fddimibPORTMACIndicated=fddimibPORTMACIndicated, fddimibSMTUserData=fddimibSMTUserData, fddimibPATHConfigTokenOrder=fddimibPATHConfigTokenOrder, fddimibSMTIndex=fddimibSMTIndex, fddimibPORTLCTFailCts=fddimibPORTLCTFailCts, fddimibMACLostCts=fddimibMACLostCts, fddimibMACDaFlag=fddimibMACDaFlag, fddimibSMTStatRptPolicy=fddimibSMTStatRptPolicy, fddimibPATHTVXLowerBound=fddimibPATHTVXLowerBound, fddimibMACNumber=fddimibMACNumber, fddimibPORTSMTIndex=fddimibPORTSMTIndex, fddimibMACTvxExpiredCts=fddimibMACTvxExpiredCts, fddimibSMTTraceMaxExpiration=fddimibSMTTraceMaxExpiration, fddimibMACFrameErrorThreshold=fddimibMACFrameErrorThreshold, fddimibPORTBSFlag=fddimibPORTBSFlag, fddimibSMTTable=fddimibSMTTable, fddimibSMTStationId=fddimibSMTStationId, fddimibPORT=fddimibPORT, fddimibSMTAvailablePaths=fddimibSMTAvailablePaths, fddimibSMTMIBVersionId=fddimibSMTMIBVersionId, fddimibSMTOpVersionId=fddimibSMTOpVersionId, fddimibMACDownstreamNbr=fddimibMACDownstreamNbr, fddimibPORTNeighborType=fddimibPORTNeighborType, fddimibPATHEntry=fddimibPATHEntry, fddimibPORTConnectState=fddimibPORTConnectState, fddimibPATHSMTIndex=fddimibPATHSMTIndex, fddimibMACCountersTable=fddimibMACCountersTable, fddimibPATHConfigResourceIndex=fddimibPATHConfigResourceIndex, fddimibPATHTable=fddimibPATHTable, fddimibMAC=fddimibMAC, fddimibSMTBypassPresent=fddimibSMTBypassPresent, fddimibMACTable=fddimibMACTable, fddi=fddi, fddimibSMT=fddimibSMT, fddimibPATHIndex=fddimibPATHIndex, fddimibSMTEntry=fddimibSMTEntry, fddimibSMTRemoteDisconnectFlag=fddimibSMTRemoteDisconnectFlag, fddimibSMTNumber=fddimibSMTNumber, fddimibMACNotCopiedCts=fddimibMACNotCopiedCts, fddimibSMTNonMasterCts=fddimibSMTNonMasterCts, fddimibPORTEntry=fddimibPORTEntry, fddimibPATHConfigCurrentPath=fddimibPATHConfigCurrentPath, fddimibMACErrorCts=fddimibMACErrorCts, fddimibPATHConfigTable=fddimibPATHConfigTable, fddimibPORTTable=fddimibPORTTable, fddimibPORTMyType=fddimibPORTMyType, fddimibMACTMax=fddimibMACTMax, fddimibSMTConfigPolicy=fddimibSMTConfigPolicy, fddimibSMTPeerWrapFlag=fddimibSMTPeerWrapFlag, fddimibPORTHardwarePresent=fddimibPORTHardwarePresent, fddimibSMTStationStatus=fddimibSMTStationStatus, fddimibPORTIndex=fddimibPORTIndex, fddimibPORTAvailablePaths=fddimibPORTAvailablePaths, fddimibPORTConnectionPolicies=fddimibPORTConnectionPolicies, fddimibMACTNeg=fddimibMACTNeg, fddimibMACUnaDaFlag=fddimibMACUnaDaFlag, fddimibSMTConnectionPolicy=fddimibSMTConnectionPolicy, FddiTimeNano=FddiTimeNano, fddimibMACCopiedCts=fddimibMACCopiedCts, fddimibSMTTNotify=fddimibSMTTNotify, fddimibPORTConnectionCapabilities=fddimibPORTConnectionCapabilities, fddimibMACRMTState=fddimibMACRMTState, fddimibPATHConfigSMTIndex=fddimibPATHConfigSMTIndex, fddimibPATHNumber=fddimibPATHNumber, fddimibPORTLerCutoff=fddimibPORTLerCutoff, fddimibMACEntry=fddimibMACEntry, fddimibPORTNumber=fddimibPORTNumber, fddimibMACRingOpCts=fddimibMACRingOpCts, fddimibPORTPMDClass=fddimibPORTPMDClass, fddimibMACTReq=fddimibMACTReq, fddimibMACRequestedPaths=fddimibMACRequestedPaths, FddiTimeMilli=FddiTimeMilli, fddimib=fddimib, fddimibSMTTransitionTimeStamp=fddimibSMTTransitionTimeStamp, FddiResourceId=FddiResourceId, FddiMACLongAddressType=FddiMACLongAddressType, fddimibMACDownstreamPORTType=fddimibMACDownstreamPORTType, fddimibSMTTimeStamp=fddimibSMTTimeStamp, fddimibSMTConfigCapabilities=fddimibSMTConfigCapabilities, fddimibPATHConfigResourceType=fddimibPATHConfigResourceType, fddimibMACIfIndex=fddimibMACIfIndex, fddimibMACUpstreamNbr=fddimibMACUpstreamNbr, fddimibMACCountersEntry=fddimibMACCountersEntry, fddimibPORTLerAlarm=fddimibPORTLerAlarm, fddimibMACOldUpstreamNbr=fddimibMACOldUpstreamNbr, fddimibSMTMasterCts=fddimibSMTMasterCts, fddimibMACIndex=fddimibMACIndex, fddimibMACTVXCapability=fddimibMACTVXCapability, fddimibPATHMaxTReq=fddimibPATHMaxTReq, fddimibPORTCurrentPath=fddimibPORTCurrentPath, fddimibPORTMACPlacement=fddimibPORTMACPlacement, fddimibPATHConfigPATHIndex=fddimibPATHConfigPATHIndex, fddimibMACFrameErrorFlag=fddimibMACFrameErrorFlag, fddimibMACDupAddressTest=fddimibMACDupAddressTest, fddimibMACTvxValue=fddimibMACTvxValue, fddimibMACLateCts=fddimibMACLateCts, fddimibMACCounters=fddimibMACCounters, fddimibMACHardwarePresent=fddimibMACHardwarePresent, fddimibSMTMACCts=fddimibSMTMACCts, fddimibPATHTMaxLowerBound=fddimibPATHTMaxLowerBound, fddimibPORTLerFlag=fddimibPORTLerFlag, fddimibSMTStationAction=fddimibSMTStationAction, fddimibMACFrameStatusFunctions=fddimibMACFrameStatusFunctions, fddimibPATHConfigEntry=fddimibPATHConfigEntry)
