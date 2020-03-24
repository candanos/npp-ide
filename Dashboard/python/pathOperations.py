import os
import pathlib
currentDir = os.getcwd()
print("currenDir:" + currentDir)
fullpath = repr("C:\Cloud\github\npp-ide\Dashboard\python\parseFullPath.py")
print("fullpath:" + fullpath)
directoryName = os.path.dirname(fullpath) 
fileName = os.path.basename(fullpath)
extension = os.path.splitext(fullpath)[1]
print(os.path.splitext(fullpath)[0])
print("directoryName:" + directoryName)
print("fileName:" + fileName)
print("extension:" + extension)
print(pathlib.Path(fullpath).suffix)
