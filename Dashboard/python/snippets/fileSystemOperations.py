import os, pathlib, shutil
from pathlib import Path

def find_allsubdirs_multipleextensions():
    # rglob means recursive glob and iterate on sub directories as well.
    directory = r'C:\npp-ide\Dashboard'
    extensions = ['ps1', 'py']
    mylist = [ file for ext in extensions for file in Path(directory).rglob(f'*{ext}')]
    for x in mylist:
        print(x)


def membersOfTheDirectory(dirPath): # iterate in a directory.
    for file in os.listdir(dirPath):
        filename = os.fsdecode(file)
        print(filename)    
        
def only_topmost_directory():
    # glob, not rglob
    ext = '.txt'
    pathlist = Path(directory_in_str).glob(f'*{ext}'))
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        # print(path_in_str)        
        
        
os.path.exists(dirName) # check if file exists

shutil.copytree(sourcePath, backupPath) # Also creates the targetPath, you backed up your folder now. It will copy an entire folder and every folder and file contained in it. 
  
shutil.copy(src, dest) # Source must represent a file but destination can be a file or a directory. If the destination is a directory then the file will be copied into destination using the base filename from source.

shutil.move(sourcePath, targetPath) # move the FILE OR FOLDER at the path source to the path destination.

shutil.rmtree(path) # will remove the folder at path, and all files and folders it contains will also be deleted.

os.unlink(path) # will delete the file at path.

os.rmdir(path) # will delete the folder at path. This folder must be empty of any files or folders.

if __name__ == '__main__':
    dirPath=r"C:/Users/CY59857/Desktop/"  
    targetPath = dirPath + "DummyFolder"
    # membersOfTheDirectory(dirPath)
    copyDirectory(dirPath, targetPath)