filePath = r'C:\Cloud\github\cobol-programs-repository-app\lists\break-down\online_members.txt'
file = open(filePath, "r")
lineList = list(dict.fromkeys(file.read().split('\n')))
lineList.sort()
file.close()
file = open(filePath, "w")
for line in lineList:
    file.write(line + '\n')
file.close()