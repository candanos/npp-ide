#!/usr/bin/python
import sys
def setFile(filePath):
	# file = open("C:/Dashboard/isbank/dbReports/report_verim_Payment_Plan.sql", "r")
	file = open(filePath, "r")
	sqlstr = file.read().replace('\n', ' ')
	x = sqlstr.split(';', 1)	
	return x[0]
    
def intoList(filePath):    
    with open(fileName) as f: lineList = f. readlines()
    return lineList
    
def intoString(filePath)    
    file = open(filePath, "r")
	sqlstr = file.read().replace('\n', ' ')	
	return sqlstr