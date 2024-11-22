


def main():

    file[0] = r'C:\Users\Candan Yuksel\Desktop\D1 (9).csv'
    file[1] = r'C:\Users\Candan Yuksel\Desktop\D1 (8).csv'
    
    file = open(filePath, "r")
    lineList = file.read().split('\n')
    file.close()
    file = open(filePath, "w+")
    print(len(lineList))
    x = 0
    max = 5000
    
    for i, line in enumerate(lineList):
        if i < max:
            file[x].write(line + '\n')
        else:
            x = x + 1     
    file.close()

    
    
if __name__ == '__main__': 
    main()