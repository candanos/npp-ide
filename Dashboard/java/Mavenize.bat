@echo off
@REM -Dfile means source file. Source file can be zip, jar, rar ...
@REM mvn install:install-file -o -s C:\JAVA\apache-maven-3.6.0\conf\settings.xml -Dfile=C:\Users\CY59857\Desktop\ibmjzos.zip ^
mvn install:install-file -o -Dfile=C:\Labs\Java\Spring_IOC.zip ^
-DgroupId=candanos.labs ^
-DartifactId=spring_IOC ^
-Dversion=1.0.0 ^
-Dpackaging=jar ^
-DcreateChecksum=true		
pause