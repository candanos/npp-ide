filePath = [None] * 10
filePath[9] = r'C:\Users\Candan Yuksel\Desktop\D1.csv'
filePath[8] = r'C:\Users\Candan Yuksel\Desktop\D1 (1).csv'
filePath[7] = r'C:\Users\Candan Yuksel\Desktop\D1 (2).csv'
filePath[6] = r'C:\Users\Candan Yuksel\Desktop\D1 (3).csv'
filePath[5] = r'C:\Users\Candan Yuksel\Desktop\D1 (4).csv'
filePath[4] = r'C:\Users\Candan Yuksel\Desktop\D1 (5).csv'
filePath[3] = r'C:\Users\Candan Yuksel\Desktop\D1 (6).csv'
filePath[2] = r'C:\Users\Candan Yuksel\Desktop\D1 (7).csv'
filePath[1] = r'C:\Users\Candan Yuksel\Desktop\D1 (8).csv'
filePath[0] = r'C:\Users\Candan Yuksel\Desktop\D1 (9).csv'

lastFile = r'C:\Users\Candan Yuksel\Desktop\mergedFile.csv'
allLines = []
for file in filePath:
    print(file)
    with open(file) as f: lineList = f.readlines()
    for line in lineList:
        allLines.append(line)

file = open(lastFile, "w")
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