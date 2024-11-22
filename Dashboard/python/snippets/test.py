from pathlib import Path

directory = r'C:\npp-ide\Dashboard'
extensions = ['ps1', 'py', 'bat']
mylist = [ file for ext in extensions for file in Path(directory).glob(f'*{ext}')]
for x in mylist:
    print(x)
    print(x.suffix)