from pathlib import Path
import os


def main():
    filepaths = []
    dirpath = r'C:\github\kola-cli\tests\cadrel\dirs\segotl5798\app\t613vcom\send_to_kola_files\archive\temp'
    dirpath = Path(dirpath).resolve()
    for item in dirpath.iterdir():
        old_name = str(item)
        new_name = old_name.replace('EXTERNAL', 'SMARTEAM')
        os.rename(old_name, new_name)
    
    
if __name__ == '__main__': 
    main()    
        