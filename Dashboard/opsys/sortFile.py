def main():    
    filePath = r'C:\Cloud\github\main-repo\cobol-programs-repository-app\scripts\01-createRepositoryMetadata\inputs\all_online_members.txt'
    filePath = r'C:\Users\A488466\Desktop\T6604120_recompiles.txt'
    file = open(filePath, "r")
    lineList = list(dict.fromkeys(file.read().split('\n')))
    lineList.sort()
    file.close()
    file = open(filePath, "w")
    for line in lineList:
        file.write(line + '\n')
    file.close()
    print(str(len(lineList)) + " lines sorted.")

if __name__ == '__main__': 
    main()    