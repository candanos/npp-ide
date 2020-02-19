@REM 
@echo off
set fullpath=C:\Labs\Java\zOS\zos-test-driver\target\
set filename=zos-test-driver-1.0-SNAPSHOT-jar-with-dependencies.jar
set toberun=%fullpath%%filename%
echo %toberun%
java -jar %toberun%
pause