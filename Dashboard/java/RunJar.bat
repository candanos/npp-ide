@REM 
@echo off
set fullpath=C:\Cloud\github\main-repo\devopz\devopz-benzoic-client\target\
set fullpath=C:\Cloud\github\doktora\target\

set filename=devopz-benzoic-client-1.0-SNAPSHOT-jar-with-dependencies.jar
set filename=doktora-0.0.1-SNAPSHOT.jar

set toberun=%fullpath%%filename% UPLOAD_AND_RUN C:\Cloud\github\main-repo\devopz\devopz-zos-resource-manager\target\devopz-zos-resource-manager-1.0.0.jar
set toberun=%fullpath%%filename%

echo %toberun%
java -jar %toberun%
pause

REM /Z22T3/usr/lpp/java/J8.0_64/bin/java -jar /u/ttg/zos-batch-submitter-bat-1.0-SNAPSHOT-jar-with-dependencies.jar