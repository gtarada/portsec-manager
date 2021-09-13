#
# PySNMP MIB module CISCO-TC (http://snmplabs.com/pysmi)
# ASN.1 source http://raw.githubusercontent.com:80/simonjj/SnmpMibs/master/CISCO-TC.mib
# Produced by pysmi-0.3.4 at Mon Sep 13 09:31:24 2021
# On host tmn-ws679 platform Linux version 4.4.0-18362-Microsoft by user gtarada
# Using Python version 3.9.7 (default, Sep 10 2021, 00:03:59) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, Unsigned32, Counter32, NotificationType, TimeTicks, MibIdentifier, ModuleIdentity, Counter64, Bits, Integer32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter32", "NotificationType", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Counter64", "Bits", "Integer32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 1))
ciscoTextualConventions.setRevisions(('2006-07-06 00:00', '2006-04-13 00:00', '2005-06-24 00:00', '2005-06-16 00:00', '2004-10-11 00:00', '2004-06-08 00:00', '2004-04-14 00:00', '2002-12-18 00:00', '2002-12-12 16:00', '2002-12-02 00:00', '2002-09-22 00:00', '2002-09-17 00:00', '2002-04-16 00:00', '2001-07-07 00:00', '2001-01-18 00:00', '2000-11-21 00:00', '1998-10-28 00:00', '1997-03-13 00:00', '1996-08-14 00:00', '1996-07-08 00:00', '1996-02-22 00:00', '1995-06-07 00:00',))
if mibBuilder.loadTexts: ciscoTextualConventions.setLastUpdated('200607060000Z')
if mibBuilder.loadTexts: ciscoTextualConventions.setOrganization('Cisco Systems, Inc.')
class Layer2Cos(TextualConvention, Integer32):
    reference = 'IEEE 802.1D, 2004 Edition, Annex G User priorities and traffic classes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class CiscoNetworkProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 65535))
    namedValues = NamedValues(("ip", 1), ("decnet", 2), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("appletalk", 7), ("clns", 8), ("lat", 9), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("ipv6", 20), ("cdm", 21), ("nbf", 22), ("bpxIgx", 23), ("clnsPfx", 24), ("http", 25), ("unknown", 65535))

class CiscoNetworkAddress(TextualConvention, OctetString):
    status = 'current'

class Unsigned64(TextualConvention, Counter64):
    status = 'current'

class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class SAPType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 254)

class CountryCode(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class CountryCodeITU(TextualConvention, Unsigned32):
    reference = 'ITU-T T.35 - Section 3.1 Country Code'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class EntPhysicalIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CiscoRowOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4))

class CiscoPort(TextualConvention, Integer32):
    reference = 'Transmission Control Protocol. J. Postel. RFC793, User Datagram Protocol. J. Postel. RFC768'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CiscoIpProtocol(TextualConvention, Integer32):
    reference = 'Internet Protocol. J. Postel. RFC791'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CiscoLocationClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("chassis", 1), ("shelf", 2), ("slot", 3), ("subSlot", 4), ("port", 5), ("subPort", 6), ("channel", 7), ("subChannel", 8))

class CiscoLocationSpecifier(TextualConvention, OctetString):
    reference = 'RFC2234, Augmented BNF for syntax specifications: ABNF'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CiscoInetAddressMask(TextualConvention, Unsigned32):
    reference = 'RFC2851, Textual Conventions for Internet Network Addresses.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 128)

class CiscoAbsZeroBasedCounter32(TextualConvention, Gauge32):
    status = 'current'

class CiscoSnapShotAbsCounter32(TextualConvention, Unsigned32):
    status = 'current'

class CiscoAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7))

class PerfHighIntervalCount(TextualConvention, Counter64):
    reference = 'RFC 2856(HCNUM-TC MIB). RFC 2493(PerfHist-TC-MIB).'
    status = 'current'

class ConfigIterator(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BulkConfigResult(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ListIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class TimeIntervalSec(TextualConvention, Unsigned32):
    status = 'current'

class TimeIntervalMin(TextualConvention, Unsigned32):
    status = 'current'

class CiscoMilliSeconds(TextualConvention, Unsigned32):
    status = 'current'

class MicroSeconds(TextualConvention, Unsigned32):
    status = 'current'

class CiscoPortList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CiscoPortListRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("oneto2k", 1), ("twoKto4K", 2), ("fourKto6K", 3), ("sixKto8K", 4), ("eightKto10K", 5), ("tenKto12K", 6), ("twelveKto14K", 7), ("fourteenKto16K", 8))

class IfOperStatusReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133))
    namedValues = NamedValues(("other", 1), ("none", 2), ("hwFailure", 3), ("loopbackDiagFailure", 4), ("errorDisabled", 5), ("swFailure", 6), ("linkFailure", 7), ("offline", 8), ("nonParticipating", 9), ("initializing", 10), ("vsanInactive", 11), ("adminDown", 12), ("channelAdminDown", 13), ("channelOperSuspended", 14), ("channelConfigurationInProgress", 15), ("rcfInProgress", 16), ("elpFailureIsolation", 17), ("escFailureIsolation", 18), ("domainOverlapIsolation", 19), ("domainAddrAssignFailureIsolation", 20), ("domainOtherSideEportIsolation", 21), ("domainInvalidRcfReceived", 22), ("domainManagerDisabled", 23), ("zoneMergeFailureIsolation", 24), ("vsanMismatchIsolation", 25), ("parentDown", 26), ("srcPortNotBound", 27), ("interfaceRemoved", 28), ("fcotNotPresent", 29), ("fcotVendorNotSupported", 30), ("incompatibleAdminMode", 31), ("incompatibleAdminSpeed", 32), ("suspendedByMode", 33), ("suspendedBySpeed", 34), ("suspendedByWWN", 35), ("domainMaxReTxFailure", 36), ("eppFailure", 37), ("portVsanMismatchIsolation", 38), ("loopbackIsolation", 39), ("upgradeInProgress", 40), ("incompatibleAdminRxBbCredit", 41), ("incompatibleAdminRxBufferSize", 42), ("portChannelMembersDown", 43), ("zoneRemoteNoRespIsolation", 44), ("firstPortUpAsEport", 45), ("firstPortNotUp", 46), ("peerFCIPPortClosedConnection", 47), ("peerFCIPPortResetConnection", 48), ("fcipPortMaxReTx", 49), ("fcipPortKeepAliveTimerExpire", 50), ("fcipPortPersistTimerExpire", 51), ("fcipPortSrcLinkDown", 52), ("fcipPortSrcAdminDown", 53), ("fcipPortAdminCfgChange", 54), ("fcipSrcPortRemoved", 55), ("fcipSrcModuleNotOnline", 56), ("invalidConfig", 57), ("portBindFailure", 58), ("portFabricBindFailure", 59), ("noCommonVsanIsolation", 60), ("ficonVsanDown", 61), ("invalidAttachment", 62), ("portBlocked", 63), ("incomAdminRxBbCreditPerBuf", 64), ("tooManyInvalidFlogis", 65), ("deniedDueToPortBinding", 66), ("elpFailureRevMismatch", 67), ("elpFailureClassFParamErr", 68), ("elpFailureClassNParamErr", 69), ("elpFailureUnknownFlowCtlCode", 70), ("elpFailureInvalidFlowCtlParam", 71), ("elpFailureInvalidPortName", 72), ("elpFailureInvalidSwitchName", 73), ("elpFailureRatovEdtovMismatch", 74), ("elpFailureLoopbackDetected", 75), ("elpFailureInvalidTxBbCredit", 76), ("elpFailureInvalidPayloadSize", 77), ("bundleMisCfg", 78), ("bitErrRuntimeThreshExceeded", 79), ("linkFailLinkReset", 80), ("linkFailPortInitFail", 81), ("linkFailPortUnusable", 82), ("linkFailLossOfSignal", 83), ("linkFailLossOfSync", 84), ("linkFailNosRcvd", 85), ("linkFailOlsRcvd", 86), ("linkFailDebounceTimeout", 87), ("linkFailLrRcvd", 88), ("linkFailCreditLoss", 89), ("linkFailRxQOverflow", 90), ("linkFailTooManyInterrupts", 91), ("linkFailLipRcvdBb", 92), ("linkFailBbCreditLoss", 93), ("linkFailOpenPrimSignalTimeout", 94), ("linkFailOpenPrimSignalReturned", 95), ("linkFailLipF8Rcvd", 96), ("linkFailLineCardPortShutdown", 97), ("fcspAuthenfailure", 98), ("fcotChecksumError", 99), ("ohmsExtLoopbackTest", 100), ("invalidFabricBindExchange", 101), ("tovMismatch", 102), ("ficonNotEnabled", 103), ("ficonNoPortNumber", 104), ("ficonBeingEnabled", 105), ("ePortProhibited", 106), ("portGracefulShutdown", 107), ("trunkNotFullyActive", 108), ("fabricBindingSwitchWwnNotFound", 109), ("fabricBindingDomainInvalid", 110), ("fabricBindingDbMismatch", 111), ("fabricBindingNoRspFromPeer", 112), ("dpvmVsanSuspended", 113), ("dpvmVsanNotFound", 114), ("trackedPortDown", 115), ("ecSuspendedOnLoop", 116), ("isolateBundleMisCfg", 117), ("noPeerBundleSupport", 118), ("portBringupIsolation", 119), ("domainNotAllowedIsolated", 120), ("virtualIvrDomainOverlapIsolation", 121), ("outOfService", 122), ("portAuthFailed", 123), ("bundleStandby", 124), ("portConnectorTypeErr", 125), ("errorDisabledReInitLmtReached", 126), ("ficonDupPortNum", 127), ("localRcf", 128), ("twoSwitchesWithSameWWN", 129), ("invalidOtherSidePrincEFPReqRecd", 130), ("domainOther", 131), ("elpFailureAllZeroPeerWWNRcvd", 132), ("preferredPathIsolation", 133))

class EntLogicalIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CiscoURLString(TextualConvention, OctetString):
    reference = 'Uniform Resource Locators. RFC 1738.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CiscoHTTPResponseStatusCode(TextualConvention, Unsigned32):
    reference = 'RFC 2616 Section 6.1.1 Status Code and Reason Phrase.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(100, 599)

class CvE164Address(TextualConvention, OctetString):
    reference = 'ITU-T E.164, Q.931 chapter 4.5.10 ITU-H H.225.0 Annex H'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

mibBuilder.exportSymbols("CISCO-TC", TimeIntervalSec=TimeIntervalSec, CiscoNetworkProtocol=CiscoNetworkProtocol, PerfHighIntervalCount=PerfHighIntervalCount, CiscoAlarmSeverity=CiscoAlarmSeverity, InterfaceIndexOrZero=InterfaceIndexOrZero, CvE164Address=CvE164Address, ciscoTextualConventions=ciscoTextualConventions, CiscoAbsZeroBasedCounter32=CiscoAbsZeroBasedCounter32, CountryCode=CountryCode, CiscoSnapShotAbsCounter32=CiscoSnapShotAbsCounter32, CiscoPort=CiscoPort, IfOperStatusReason=IfOperStatusReason, MicroSeconds=MicroSeconds, ListIndexOrZero=ListIndexOrZero, CiscoNetworkAddress=CiscoNetworkAddress, CiscoPortListRange=CiscoPortListRange, CiscoURLString=CiscoURLString, CiscoIpProtocol=CiscoIpProtocol, CiscoHTTPResponseStatusCode=CiscoHTTPResponseStatusCode, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, EntLogicalIndexOrZero=EntLogicalIndexOrZero, SAPType=SAPType, BulkConfigResult=BulkConfigResult, ListIndex=ListIndex, ConfigIterator=ConfigIterator, CiscoMilliSeconds=CiscoMilliSeconds, Unsigned64=Unsigned64, CiscoInetAddressMask=CiscoInetAddressMask, TimeIntervalMin=TimeIntervalMin, Layer2Cos=Layer2Cos, CiscoLocationClass=CiscoLocationClass, PYSNMP_MODULE_ID=ciscoTextualConventions, CountryCodeITU=CountryCodeITU, CiscoPortList=CiscoPortList, CiscoLocationSpecifier=CiscoLocationSpecifier, CiscoRowOperStatus=CiscoRowOperStatus)
