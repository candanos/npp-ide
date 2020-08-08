import subprocess
# sourcePath = 'CY59857.TEXT0001'
# targetPath = r'C:/Users/CY59857/Desktop/zosFile.txt'
     
   # create | cre  Create data sets
   # delete | del  Delete a data set or Unix System Services file
   # download | dl Download content from z/OS data sets and USS files
   # invoke | call Invoke various z/OS utilities
   # list | ls     List the details for data sets and the members in the data sets
   # upload | ul   Upload the contents of a file to z/OS data sets
def main():
    # getDataSetFromZos()
    sendFileToZos()
    
def getDataSetFromZos():
   # zowe zos-files download
   # all-members | am Download all members from a pds
   # data-set | ds    Download content from a z/OS data set
   # uss-file | uf    Download content from a USS file
    sourcePath = r'/u/xlrint1/.profile'
    targetPath = r'C:/Users/CY59857/Desktop/xlrint.profile'
    subprocess.call(([r'C:\Users\CY59857\AppData\Roaming\npm\zowe.cmd', 'zos-files', 'download', 'uf', sourcePath, '-f', targetPath]))
    
def sendFileToZos():
   # zowe zos-files upload
   # dir-to-pds | dtp         Upload files from a local directory to a partitioned data set (PDS)                         
   # dir-to-uss | dtu         Upload a local directory to a USS directory
   # file-to-data-set | ftds  Upload the contents of a file to a z/OS data set
   # file-to-uss | ftu        Upload content to a USS file from local file
   # stdin-to-data-set | stds Upload the content of a stdin to a z/OS data set
    sourcePath =r'C:/Users/CY59857/Desktop/EbcdicRepos/varlik-yonetimi-app/COBOL'
    targetPath = r'/u/BT/CY59857/.profile'
    targetPath = r'SBTEKNIK.SCORETFS.COBOL'
   
    subprocess.call(([r'C:\Users\CY59857\AppData\Roaming\npm\zowe.cmd', 'zos-files', 'upload', 'dtp', sourcePath,  targetPath, '--binary']))
   
if __name__ == '__main__':
    main()
   