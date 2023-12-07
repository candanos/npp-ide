from PyPDF2 import PdfFileMerger, PdfFileReader
merger = PdfFileMerger()

filename01=r'C:\Cloud\GoogleDrive\Master\library\IT Library\IDEA\merged.pdf'
filename02=r'C:\Cloud\GoogleDrive\Master\library\IT Library\IDEA\20.pdf'
filename03=r'C:\Cloud\GoogleDrive\Master\library\IT Library\IDEA\21.pdf'



merger.append(PdfFileReader(open(filename01, 'rb')))
merger.append(PdfFileReader(open(filename02, 'rb')))
merger.append(PdfFileReader(open(filename03, 'rb')))

merger.write("C:\Cloud\GoogleDrive\Master\library\IT Library\IDEA\merged.pdf")