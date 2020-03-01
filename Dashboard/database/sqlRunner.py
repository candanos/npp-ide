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
resultFolder = Path("C:/Users/Candan Yuksel/Desktop/")
resultFl='result_' + sqlFileName + '_' + mydate + '.csv' 
sqlFile = sqlFilePath + '/' + sqlFileName
resultFl = resultFolder / resultFl
typ = sqlFileName.split("_")[0]

conn = dbConnections.getConnection(typ)
curs = conn.cursor()
sqlStr = getSqlFromFile.setFile(sqlFile)
print(sqlStr)
curs.execute(sqlStr)

lst = []
cols = []
for row in curs.description:
	cols.append(row[0])
lst.append(cols)

for row in curs:
    print(row)
    lst.append(row)
	
print(len(lst))
csv.register_dialect('semicol', delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')

with open(resultFl, 'w', newline='') as f:
    writer = csv.writer(f, 'semicol')
    writer.writerows(lst)
	
conn.close()			