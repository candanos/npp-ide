
def main():
    filePath = r'C:\Cloud\github\cobol-programs-repository-app\scripts\createRepositoryMetadata\inputs\members_of_02_rotatif-krediler-hesap-yonetimi.txt'
    file = open(filePath, "r")
    lineList = list(dict.fromkeys(file.read().split('\n')))
    file.close()
    file = open(filePath, "w")

    for line in lineList:
        line = formatLine(line)
        file.write(line + '\n')
    
    file.close()

def formatLine(line):
    #some string operations.
    return line
    
    
if __name__ == '__main__': 
    main()    
    
    