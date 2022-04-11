import os 
import sys
import subprocess

javaFilePath = sys.argv[1]
javaFileName = sys.argv[2]

print(javaFileName)
print(javaFilePath)

sourcepath = ""
targetpath = ""
classpath = ""
# compiler_command = "javac -d " + targetpath + " -sourcepath "  + sourcepath + " -cp  " + classpath + " " + javaFileName
compiler_command = "javac " + javaFilePath + "\\" + javaFileName
# res = os.system(compiler_command)
print(compiler_command)
subprocess.run([compiler_command])
