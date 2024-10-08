def main():
    filePath0 = r'C:\Cloud\github\main-repo\cobol-programs-repository-app\scripts\01-createRepositoryMetadata\inputs\all_members.txt'
    filePath1 = r'C:\Cloud\github\main-repo\cobol-programs-repository-app\scripts\01-createRepositoryMetadata\inputs\all_online_members.txt'
    
    lastFile = r'C:\Users\Candan Yuksel\Desktop\extractedFile.csv'
    remainingLines = []
    file0Lines = []
    file1Lines = []

    with open(filePath0) as f: lineList = f.readlines()
    for line in lineList:
        file0Lines.append(line)
    
    with open(filePath1) as f: lineList = f.readlines()
    for line in lineList:
        file1Lines.append(line)
    
    print(len(file0Lines))
    print(len(file1Lines))
    for line0 in file0Lines: # bigger file 
        status="notFound"
        for line1 in file1Lines: # smaller file 
            if line0.rstrip() == line1.rstrip():
                status="found"
                break       
        if status == "notFound":
            # print(line1 + " " + status) 
            remainingLines.append(line0)
        
    file = open(lastFile, "w")
    for line in remainingLines:
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