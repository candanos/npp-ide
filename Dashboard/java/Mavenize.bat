@echo off
@REM -Dfile means source file. Source file can be zip, jar, rar ...
@REM mvn install:install-file -o -s C:\JAVA\apache-maven-3.6.0\conf\settings.xml -Dfile=C:\Users\CY59857\Desktop\ibmjzos.zip ^
REM call "C:\JAVA\apache-maven-3.6.3\bin\mvn" install:install-file -o -Dfile=C:\Cloud\github\main-repo\devopz\devopz-jgit-util\target\devopz-jgit-util-1.0-SNAPSHOT.jar -DgroupId=com.isbank -DartifactId=devopz-jgit-util -Dversion=1.0.0 -Dpackaging=jar -DcreateChecksum=true

REM call "C:\JAVA\apache-maven-3.6.3\bin\mvn" install:install-file -o -Dfile=C:\Java\externalJars\db2jcc4.jar -DgroupId=com.isbank -DartifactId=db2jcc4 -Dversion=1.0.0 -Dpackaging=jar -DcreateChecksum=true

call "C:\JAVA\apache-maven-3.6.3\bin\mvn" install:install-file -o -Dfile=C:\Java\externalJars\db2jcc_license_cisuz.jar -DgroupId=com.isbank -DartifactId=db2jcc_license_cisuz -Dversion=1.0.0 -Dpackaging=jar -DcreateChecksum=true
pause