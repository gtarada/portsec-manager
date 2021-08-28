#
# PySNMP MIB module CISCO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source http://raw.githubusercontent.com:80/simonjj/SnmpMibs/master/CISCO-SMI.mib
# Produced by pysmi-0.3.4 at Sat Aug 28 16:40:29 2021
# On host thinkpad platform Linux version 4.4.0-19041-Microsoft by user gtarada
# Using Python version 3.9.5 (default, May 19 2021, 11:32:47) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, TimeTicks, ModuleIdentity, Counter32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ObjectIdentity, enterprises, IpAddress, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Counter32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ObjectIdentity", "enterprises", "IpAddress", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(('2000-01-11 00:00', '1997-04-09 00:00', '1995-05-16 00:00', '1994-04-26 20:00',))
if mibBuilder.loadTexts: cisco.setLastUpdated('200001110000Z')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
ciscoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 1))
if mibBuilder.loadTexts: ciscoProducts.setStatus('current')
local = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 2))
if mibBuilder.loadTexts: local.setStatus('current')
temporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 3))
if mibBuilder.loadTexts: temporary.setStatus('current')
pakmon = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 4))
if mibBuilder.loadTexts: pakmon.setStatus('current')
workgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 5))
if mibBuilder.loadTexts: workgroup.setStatus('current')
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6))
if mibBuilder.loadTexts: otherEnterprises.setStatus('current')
ciscoAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 7))
if mibBuilder.loadTexts: ciscoAgentCapability.setStatus('current')
ciscoConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 8))
if mibBuilder.loadTexts: ciscoConfig.setStatus('current')
ciscoMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9))
if mibBuilder.loadTexts: ciscoMgmt.setStatus('current')
ciscoExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10))
if mibBuilder.loadTexts: ciscoExperiment.setStatus('current')
ciscoAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11))
if mibBuilder.loadTexts: ciscoAdmin.setStatus('current')
ciscoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 12))
if mibBuilder.loadTexts: ciscoModules.setStatus('current')
lightstream = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 13))
if mibBuilder.loadTexts: lightstream.setStatus('current')
ciscoworks = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 14))
if mibBuilder.loadTexts: ciscoworks.setStatus('current')
newport = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 15))
if mibBuilder.loadTexts: newport.setStatus('current')
ciscoPartnerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 16))
if mibBuilder.loadTexts: ciscoPartnerProducts.setStatus('current')
ciscoPolicy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17))
if mibBuilder.loadTexts: ciscoPolicy.setStatus('current')
ciscoPIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17, 2))
if mibBuilder.loadTexts: ciscoPIB.setStatus('current')
ciscoPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18))
if mibBuilder.loadTexts: ciscoPolicyAuto.setStatus('current')
ciscoPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18, 2))
if mibBuilder.loadTexts: ciscoPibToMib.setStatus('current')
ciscoProxy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 1))
if mibBuilder.loadTexts: ciscoProxy.setStatus('current')
ciscoPartyProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 1))
ciscoContextProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 2))
ciscoRptrGroupObjectID = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2))
if mibBuilder.loadTexts: ciscoRptrGroupObjectID.setStatus('current')
ciscoUnknownRptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 1))
if mibBuilder.loadTexts: ciscoUnknownRptrGroup.setStatus('current')
cisco2505RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 2))
if mibBuilder.loadTexts: cisco2505RptrGroup.setStatus('current')
cisco2507RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 3))
if mibBuilder.loadTexts: cisco2507RptrGroup.setStatus('current')
cisco2516RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 4))
if mibBuilder.loadTexts: cisco2516RptrGroup.setStatus('current')
ciscoWsx5020RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 5))
if mibBuilder.loadTexts: ciscoWsx5020RptrGroup.setStatus('current')
ciscoChipSets = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3))
if mibBuilder.loadTexts: ciscoChipSets.setStatus('current')
ciscoChipSetSaint1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 1))
if mibBuilder.loadTexts: ciscoChipSetSaint1.setStatus('current')
ciscoChipSetSaint2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 2))
if mibBuilder.loadTexts: ciscoChipSetSaint2.setStatus('current')
ciscoChipSetSaint3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 3))
if mibBuilder.loadTexts: ciscoChipSetSaint3.setStatus('current')
ciscoChipSetSaint4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 4))
if mibBuilder.loadTexts: ciscoChipSetSaint4.setStatus('current')
mibBuilder.exportSymbols("CISCO-SMI", cisco2516RptrGroup=cisco2516RptrGroup, ciscoRptrGroupObjectID=ciscoRptrGroupObjectID, PYSNMP_MODULE_ID=cisco, newport=newport, ciscoPIB=ciscoPIB, ciscoAdmin=ciscoAdmin, ciscoExperiment=ciscoExperiment, ciscoWsx5020RptrGroup=ciscoWsx5020RptrGroup, local=local, cisco2507RptrGroup=cisco2507RptrGroup, ciscoChipSetSaint3=ciscoChipSetSaint3, pakmon=pakmon, otherEnterprises=otherEnterprises, ciscoPartyProxy=ciscoPartyProxy, ciscoPolicyAuto=ciscoPolicyAuto, temporary=temporary, workgroup=workgroup, cisco2505RptrGroup=cisco2505RptrGroup, ciscoPolicy=ciscoPolicy, ciscoChipSetSaint1=ciscoChipSetSaint1, ciscoChipSets=ciscoChipSets, ciscoModules=ciscoModules, ciscoworks=ciscoworks, lightstream=lightstream, ciscoContextProxy=ciscoContextProxy, ciscoAgentCapability=ciscoAgentCapability, ciscoUnknownRptrGroup=ciscoUnknownRptrGroup, ciscoPartnerProducts=ciscoPartnerProducts, ciscoChipSetSaint4=ciscoChipSetSaint4, ciscoPibToMib=ciscoPibToMib, cisco=cisco, ciscoChipSetSaint2=ciscoChipSetSaint2, ciscoConfig=ciscoConfig, ciscoProducts=ciscoProducts, ciscoMgmt=ciscoMgmt, ciscoProxy=ciscoProxy)
