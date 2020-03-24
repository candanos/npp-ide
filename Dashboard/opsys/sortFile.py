filePath = r'C:\Users\Candan Yuksel\Desktop\formattedFile.csv'
file = open(filePath, "r")
lineList = list(dict.fromkeys(file.read().split('\n')))
lineList.sort()
file.close()
file = open(filePath, "w")
for line in lineList:
    file.write(line + '\n')
file.close()