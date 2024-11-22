#!/usr/bin/python
import sys
import os 
    
sample_filapath = r'C:\npp-ide\Dashboard'
    
def readIntoList(filePath):    
    with open(fileName) as f: lineList = f. readlines()
    return lineList
    
def readIntoList(reportfl):
    lineArr = [line.rstrip('\n').rstrip(' ') for line in open(reportfl)]
    return lineArr
    
def readIntoString(filePath):    
    file = open(filePath, "r", encoding='UTF-8')
	sqlstr = file.read().replace('\n', ' ')	
	return sqlstr
    
def readIntoString(filePath):        
    tmp = " "
    return tmp.join([line.rstrip('\n').rstrip(' ') for line in open(searchFileFullPath)])
    
def writeArrayAsLines(filePath, array):    
    f= open(filePath, "w+", encoding='UTF-8', newline='\n') # newline='\n' if you don't want CRLF
    for line in array:
        f.write(line + '\n') 
    f.close() 
    
def writeArrayAsLines(filePath, array):    
    f= open(filePath, "w+", encoding='UTF-8', newline='\n') # newline='\n' if you don't want CRLF
    f.writeLines(array)
    f.close()     
    
    