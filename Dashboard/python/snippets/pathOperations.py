import os
import pathlib
currentDir = os.getcwd()
print("currenDir:" + currentDir)
fullpath = repr("C:\Cloud\github\npp-ide\Dashboard\python\parseFullPath.py")
print("fullpath:" + fullpath)
directoryName = os.path.dirname(fullpath) 
print("directoryName:" + directoryName)
fileName = os.path.basename(fullpath) #sadece dosya adı ve uzantısı
extension = os.path.splitext(fullpath)[1]
print("fileName:" + fileName)
print("extension:" + extension)
print(pathlib.Path(fullpath).suffix)

# if filename.endswith('.rxt'):

# Edit sys.path in windows
# each One of three typing works
# sys.path.append('C:\\github\\kola-cli\\src')
# sys.path.append(r'C:/github/kola-cli/src')
sys.path.append(r'C:\github\kola-cli\src')

from api.dto.w2k import w2kDTO
