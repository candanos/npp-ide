from zeep import Client
from zeep import xsd

# client = Client('http://localhost:8080/bebop/darkjobs?wsdl')

client = Client('http://10.200.14.1:29080/bebop/darkjobs?wsdl')


# ddname = "cy590001" 
# dsn = "SBTEKNIK.SCORETFS.LM03"
# cmd = "alloc fi(" + ddname + ") da(" + dsn + ") reuse new " 
# cmd = cmd + "space(1000,100) tracks catalog dsorg(PO) lrecl(80) recfm(f,b) dsntype(library) msg(wtp)"
# cmd = "free fi(" + ddname + ") msg(wtp)"
# cmd = "alloc fi(" + ddName + ") da(" + targetDSN + ") reuse new " 
# cmd = cmd + "space(1000,100) tracks catalog dsorg(PO) blksize(4096) dataclas(data) lrecl(23200) recfm(u) dsntype(library) msg(wtp)"
# result = client.service.runBPXWDYN(cmd)
# print("result" + ":" + result)
# cmd = "free fi(" + ddname + ") msg(wtp)"
# result = client.service.runBPXWDYN(cmd)
# print("result" + ":" + result)

dsn = "//'SBCOMMON.PROD.COBOL'"
dsn = "SBCOMMON.PROD.COBOL"
dsn = "'SBCOMMON.PROD.COBOL'"
result = client.service.checkZFileExists(dsn)
print("result" + ":" + result)



# System.getProperty("user.home") 
# System.getProperty("user.dir") 
# System.getProperty("java.home")
# System.getProperty("java.class.path");
