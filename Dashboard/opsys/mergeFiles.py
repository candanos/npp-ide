def main():
    filePath = [None] * 4
    filePath[3] = r'C:\Users\A488466\Desktop\unbridged_nonVCE_4.csv'
    filePath[2] = r'C:\Users\A488466\Desktop\unbridged_nonVCE_3.csv'
    filePath[1] = r'C:\Users\A488466\Desktop\unbridged_nonVCE_2.csv'
    filePath[0] = r'C:\Users\A488466\Desktop\unbridged_nonVCE_1.csv'
    
    lastFile = r'C:\Users\A488466\Desktop\unbridged_nonVCE.csv'
    allLines = []
    for file in filePath:
        print(file)
        with open(file) as f: lineList = f.readlines()
        for line in lineList[1:]:
            allLines.append(line)
    
    file = open(lastFile, "w+")
    for line in allLines:
        file.write(line)
    file.close()
    
    # file = open(filePath, "r")
    # lineList = list(dict.fromkeys(file.read().split('\n')))
    # lineList.sort()
    # file.close()
    # file = open(filePath, "w")
    # for line in lineList:
        # file.write(line + '\n')
    # file.close()

if __name__ == '__main__': 
    main()    