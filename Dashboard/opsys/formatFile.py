from pathlib import Path

def main():
    # filepaths = []
    # filepaths[0] = r'C:\Users\Candan Yuksel\Desktop\extractedFile.csv'
    # filepaths[1] = r'C:\Users\A488466\Desktop\Arquus_DesignLocation\temp2.txt'
    # filepaths[2] = r'C:\github\part-foundation-candanos\all_xml_files_done_signal_types.txt'
    # filepaths[3] = r'C:\Users\A488466\OneDrive - Volvo Group\Workspace\FGI\excel_list.csv'
    # filepaths[4] = r'C:\Users\A488466\Desktop\smart.txt'
    
    # filepaths = []
    # dirpath = r'C:\github\kola-cli\tests\cadrel\dirs\segotl5798\app\t613vcom\send_to_kola_files\archive\segotl2804_done'
    # dirpath = Path(dirpath).resolve()
    # for item in dirpath.iterdir():
        # filepaths.append(str(item))
        # print(item)
        
    filepaths = []
    listfile = Path(r'C:\github\kola-cli\tests\cadrel\dirs\upload\uploadlist.txt')
    file = open(listfile, "r")
    filelist = file.read().split('\n')
    file.close()
    dirpath = Path(r'C:\github\kola-cli\tests\cadrel\dirs\segotl5798\app\t613vcom\send_to_kola_files\archive\done')
    # for filename in filelist[:10]:
    for filename in filelist:
        filePath = dirpath.joinpath(filename)
        
        file = open(filePath, "r")
        # by removing duplicates
        # lineList = list(dict.fromkeys(file.read().split('\n')))
        # without removing duplicates
        lineList = file.read().split('\n')
        file.close()
        
        outfile = filePath #edit same file
        outpath = Path(r'C:\github\kola-cli\tests\cadrel\dirs\segotl5798\app\t613vcom\send_to_kola_files\archive\temp')
        outfile = outpath.joinpath(filename) #use a different formatted file
        
        file = open(outfile, "w")
        for line in lineList:
            line = formatLine(line)
            file.write(line + '\n')
        file.close()
    
    
def formatLine(line):
    #some string operations.
    # return line #means removing duplicates.
    # line = line.rstrip()
    # line.split(',')[0]
    # line.split(',')[1]
    # itemno = line.split(';')[0].rjust(8, '0') # insert zeros to left
    first = "<organization>ARQUUS</organization>"
    second = "<lifecycle_status>FF</lifecycle_status>"
    if first in line:
        line = line + '\n' + line.replace(first, second)
    return line
    
    
if __name__ == '__main__': 
    main()    
    
# item_subtypes = {
# 'A':'D',
# 'J':'D',
# 'M':'D',
# 'N':'D',
# 'R':'D',
# 'T':'D',
# 'U':'D',
# '7':'D',
# '8':'D',
# '9':'D',
# 'G':'I',
# 'H':'I',
# 'L':'I',
# 'Q':'I',
# 'V':'I',
# 'W':'I',
# '1':'I',
# '3':'I',
# '6':'I',
# 'O':'M',
# '2':'M',
# '5':'M',
# 'B':'P',
# 'C':'P',
# 'D':'P',
# 'E':'P',
# 'F':'P',
# 'I':'P',
# 'K':'P',
# 'P':'P',
# 'S':'P',
# 'X':'P',
# 'Y':'P'
# }
