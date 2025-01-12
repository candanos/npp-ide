#!/usr/bin/python
import os
# import cx_Oracle
# import mysql
# from mysql import connector
# from mysql.connector import Error
# import jaydebeapi  
import pyodbc

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

def db2_JDBC_ConnC():
    jar1 = r'C:\database\db2jcc4.jar'
    jar2 = r'C:\database\db2jcc_license_cisuz.jar'
    os.environ["CLASSPATH"] = jar1 + ";" + jar2
    jclassname = 'com.ibm.db2.jcc.DB2Driver'
    url = 'jdbc:db2://dv0bdb2.isbank:446/DV0BPLOC'
    # host = 'dv0bdb2.isbank'
    print(os.environ["CLASSPATH"]) 
    os.environ["CLASSPATH"] = os.environ["CLASSPATH"] + ";" + jar1 + ";" + jar2
    print(os.environ["CLASSPATH"]) 
    username = 'cy59857'
    password = 'o3o3o3o3'

    connection = jaydebeapi.connect(jclassname, url, {'user': username, 'password': password}, jars=[jar1,jar2])
    return connection

def db2_ODBC_conn():
    print("our KOLA")
    connstr = 'DSN=D20Q; UID=A488466;PWD=o4o4o4o4'
    connstr = 'DSN=D20H; UID=A488466;PWD=o4o4o4o4'
    connstr = 'DSN=D2TP; UID=A488466;PWD=o6o6o6o6'
    connection = pyodbc.connect(connstr)
    print('connected')
    # cnxn = pyodbc.connect("DSN=BCTHEAT")
    # cursor = cnxn.cursor()
    # cursor.execute("select * from acr.Table_one_hh")
    # row = cursor.fetchall()
    return connection
    
def getConnection(typ):        
    if(typ == 'eufb'):
        conn = mysqlConn()
        return conn
    if(typ == 'db2'):
        conn = db2Conn()
        return conn     
    if(typ == 'kola'):
        print("it is KOLA")
        conn = db2_ODBC_conn()
        return conn     



    