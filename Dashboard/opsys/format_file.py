from pathlib import Path

def readfile(filepath):
    file = open(filepath, "r")
    linelist = file.read().split('\n')
    file.close()
    return linelist


def writefile(filepath, linelist):
    file = open(filepath, "w")
    for line in linelist:
        file.write(line + '\n')
    file.close()

    
def remove_duplicate_lines(linelist):
    linelist = list(dict.fromkeys(linelist))  
    return linelist 

 
def insert_zeros_left(linelist):
    formatted_linelist = []
    for line in linelist:
        first = line.rstrip().split(' ')[0]
        second = first.rjust(8, '0')
        line = line.replace(first, second)
        formatted_linelist.append(line)    
    return formatted_linelist 

    
def addline(line):
    first = "<organization>ARQUUS</organization>"
    second = "<lifecycle_status>FF</lifecycle_status>"
    if first in line:
        line = line + '\n' + line.replace(first, second)
    return line
    
    
if __name__ == '__main__': 
    filepath = Path(r'C:\npp-ide\Dashboard\workspace\documents_to_remove_markedForArquus.txt')    
    filepath_formatted = Path(r'C:\npp-ide\Dashboard\workspace\documents_to_remove_markedForArquus_formatted.txt')
    
    linelist = readfile(filepath)
    
    # linelist = remove_duplicate_lines(linelist)
    linelist = insert_zeros_left(linelist)
    
    writefile(filepath_formatted, linelist)
