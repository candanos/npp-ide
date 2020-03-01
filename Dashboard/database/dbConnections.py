#!/usr/bin/python
import os
import cx_Oracle
import mysql
from mysql import connector
from mysql.connector import Error
def mysqlConn():
    try:
        connection = mysql.connector.connect(host='localhost',
                                    database='dbeurofootball',
                                    user='root',
                                    password='xxxx')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            return connection 
            # cursor = connection.cursor()
            # cursor.execute("select database();")
            # record = cursor.fetchone()
            # print("You're connected to database: ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)
    # finally:
        # if (connection.is_connected()):
            # cursor.close()
            # connection.close()
            # print("MySQL connection is closed")      

def getConnection(typ):        
    if(typ == 'eufb'):
        print('db type = mysql')
        conn = mysqlConn()
        return conn
    if(typ == 'db2'):
        conn == db2Conn()
        return conn     



    