#!/usr/bin/python
import os
# import cx_Oracle
import dbConnections
import getSqlFromFile
import sys
import csv
import datetime
from pathlib import Path

                
sqlFilePath = sys.argv[1]
sqlFileName = sys.argv[2]
mydate = datetime.datetime.now().strftime('%H%M%S')
resultFolder = Path("C:/Users/A488466/Desktop/")
resultFolder = os.getcwd()
resultFl='result_' + sqlFileName + '_' + mydate + '.csv' 
sqlFile = sqlFilePath + '/' + sqlFileName
resultFl = resultFolder + '/' +  resultFl
typ = sqlFileName.split("_")[0]

conn = dbConnections.getConnection(typ)
print('got connection')
curs = conn.cursor()
sqlStr = getSqlFromFile.setFile(sqlFile)
print(sqlStr)
curs.execute(sqlStr)


lst = []
cols = []
lst.append(str(sqlStr))

if curs.description:
    columns = [column[0] for column in curs.description]
    print(columns)
    if(typ=='db2'):
        result = curs.fetchall()
        for row in result:
            print(row)
            lst.append(row)
    elif(typ=='kola'):
        result = curs.fetchall()
        for row in result:
            print(row)
            lst.append(row)
    else:   
        for row in curs:
            print(row)
            lst.append(row)

conn.commit()

conn.close()

# print(len(lst))
# csv.register_dialect('semicol', delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
# print(resultFl)
# with open(resultFl, 'w', newline='') as f:
    # writer = csv.writer(f, 'semicol')
    # writer.writerows(lst)
	
			