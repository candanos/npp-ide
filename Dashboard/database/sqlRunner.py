#!/usr/bin/python
import os
import cx_Oracle
import dbConnections
import getSqlFromFile
import sys
import csv
import datetime
from pathlib import Path
                
sqlFilePath = sys.argv[1]
sqlFileName = sys.argv[2]
mydate = datetime.datetime.now().strftime('%H%M%S')
resultFolder = Path("C:/Users/CY59857/Desktop/")
resultFolder = os.getcwd()
resultFl='result_' + sqlFileName + '_' + mydate + '.csv' 
sqlFile = sqlFilePath + '/' + sqlFileName
resultFl = resultFolder + '/' +  resultFl
typ = sqlFileName.split("_")[0]

conn = dbConnections.getConnection(typ)
curs = conn.cursor()
sqlStr = getSqlFromFile.setFile(sqlFile)
print(sqlStr)
curs.execute(sqlStr)


# result = curs.fetchall()

lst = []
cols = []
for row in curs.description:
	cols.append(row[0])
lst.append(cols)

if(typ=='db2'):
    result = curs.fetchall()
    for row in result:
        print(row)
        lst.append(row)
else:   
    for row in curs:
        print(row)
        lst.append(row)


print(len(lst))
csv.register_dialect('semicol', delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
print(resultFl)
with open(resultFl, 'w', newline='') as f:
    writer = csv.writer(f, 'semicol')
    writer.writerows(lst)
	
conn.close()			