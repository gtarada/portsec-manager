"""
Compile MIBs from web
+++++++++++++++++++++
Look up specific ASN.1 MIBs at configured Web and FTP sites,
compile them into pysnmp form and save Python modules as plain-text
files in a local directory.
Try to support both SMIv1 and SMIv2 flavors of SMI as well as
popular deviations from official syntax found in the wild.
In this example we disable automatic dependency checking on MIB
compilation using noDeps flag.
Also, we do not check if target file already exists thus MIB
compilation occurs on every invocation.
"""  #
# from pysnmp import debug
from pysmi.reader import HttpReader
from pysmi.reader import FtpReader
from pysmi.searcher import StubSearcher
from pysmi.writer import PyFileWriter
from pysmi.parser import SmiStarParser
from pysmi.codegen import PySnmpCodeGen
from pysmi.compiler import MibCompiler
from pysmi import debug
import logging
import sys

debug.setLogger(debug.Debug("all"))
formatting = "[%(asctime)s-%(levelname)s]-(%(module)s) %(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatting)

inputMibs = [
    "CISCO-STACK-MIB",
    "IF-MIB"
]
httpSources = [
    # ("mibs.snmplabs.com", 80, "/asn1/@mib@"),
    ("raw.githubusercontent.com", 80, "/simonjj/SnmpMibs/master/@mib@"),
    ("www.circitor.fr", 80, "/Mibs/Mib/C/@mib@"),
    ("www.circitor.fr", 80, "/Mibs/Mib/E/@mib@"),
    ("www.circitor.fr", 80, "/Mibs/Mib/F/@mib@"),
    ("www.circitor.fr", 80, "/Mibs/Mib/I/@mib@"),
    ("www.circitor.fr", 80, "/Mibs/Mib/R/@mib@"),
    ("www.circitor.fr", 80, "/Mibs/Mib/S/@mib@"),
    ("www.circitor.fr", 80, "/Mibs/Mib/T/@mib@"),

]
ftpSources = [
    ("ftp.cisco.com", "/pub/mibs/v2/@mib@"),
    ("ftp.cisco.com", "/pub/mibs/v1/@mib@"),
]
dstDirectory = "./mibs"
# Initialize compiler infrastructure
mibCompiler = MibCompiler(SmiStarParser(), PySnmpCodeGen(), PyFileWriter(dstDirectory))
# search for source MIBs at Web and FTP sites
mibCompiler.addSources(*[HttpReader(*x) for x in httpSources])
mibCompiler.addSources(*[FtpReader(*x) for x in ftpSources])
# never recompile MIBs with MACROs
mibCompiler.addSearchers(StubSearcher(*PySnmpCodeGen.baseMibs))
# run recursive MIB compilation
results = mibCompiler.compile(*inputMibs, **dict(noDeps=False))

print("Results: %s" % ", ".join(["%s:%s" % (x, results[x]) for x in results]))
