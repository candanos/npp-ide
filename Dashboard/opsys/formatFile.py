
def main():
    filePath = r'C:\Users\Candan Yuksel\Desktop\extractedFile.csv'
    file = open(filePath, "r")
    lineList = list(dict.fromkeys(file.read().split('\n')))
    file.close()
    file = open(filePath, "w")
    print(len(lineList))
    for line in lineList:
        line = formatLine(line)
        file.write(line + '\n')
    
    file.close()

def formatLine(line):
    #some string operations.
    line = line.rstrip()
    return line
    
    
if __name__ == '__main__': 
    main()    
    
    