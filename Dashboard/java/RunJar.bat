@REM 
@echo off
set fullpath=C:\Cloud\github\zos-batch-submitter-bat\target\
set filename=zos-batch-submitter-bat-1.0-SNAPSHOT.jar
set toberun=%fullpath%%filename%
echo %toberun%
java -jar %toberun%
pause

REM /Z22T3/usr/lpp/java/J8.0_64/bin/java -jar /u/ttg/zos-batch-submitter-bat-1.0-SNAPSHOT-jar-with-dependencies.jar