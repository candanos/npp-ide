
item_subtypes = {
'A':'D',
'J':'D',
'M':'D',
'N':'D',
'R':'D',
'T':'D',
'U':'D',
'7':'D',
'8':'D',
'9':'D',
'G':'I',
'H':'I',
'L':'I',
'Q':'I',
'V':'I',
'W':'I',
'1':'I',
'3':'I',
'6':'I',
'O':'M',
'2':'M',
'5':'M',
'B':'P',
'C':'P',
'D':'P',
'E':'P',
'F':'P',
'I':'P',
'K':'P',
'P':'P',
'S':'P',
'X':'P',
'Y':'P'
}


def main():
    filePath = r'C:\Users\Candan Yuksel\Desktop\extractedFile.csv'
    filePath = r'C:\Users\A488466\Desktop\Arquus_DesignLocation\temp2.txt'
    filePath = r'C:\github\part-foundation-candanos\all_xml_files_done_signal_types.txt'
    
    file = open(filePath, "r")
    # by removing duplicates
    # lineList = list(dict.fromkeys(file.read().split('\n')))
    # without removing duplicates
    lineList = file.read().split('\n')
    file.close()
    file = open(filePath, "w")
    print(len(lineList))
    for line in lineList:
        line = formatLine(line)
        file.write(line + '\n')
    
    file.close()

def formatLine(line):
    #some string operations.
    return line #means removing duplicates.
    line = line.rstrip()
    print(line)
    line.split(',')[0]
    line.split(',')[1]
    itemno = line.split(',')[0].rjust(8, '0')
    type = item_subtypes[line.split(',')[1]]
    line=f"{type}{itemno}"
    return line
    
    
if __name__ == '__main__': 
    main()    
    
    