@echo off
@REM -Dfile means source file. Source file can be zip, jar, rar ...
@REM mvn install:install-file -o -s C:\JAVA\apache-maven-3.6.0\conf\settings.xml -Dfile=C:\Users\CY59857\Desktop\ibmjzos.zip ^
mvn install:install-file -o -Dfile=C:\JAVA\repositories\ibmjzos.jar ^
-DgroupId=com.ibm ^
-DartifactId=ibmjzos ^
-Dversion=1.0.0 ^
-Dpackaging=jar ^
-DcreateChecksum=true		
pause