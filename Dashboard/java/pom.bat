@REM To run with: exec-this.bat $(CURRENT_DIRECTORY) $(FILE_NAME)
echo "this is pom.bat"
@echo off
@set a=%2
@set x="x"
for /F "tokens=1 delims=." %%N IN ("%a%") DO set name=%%N  
for /F "tokens=2 delims=." %%T IN ("%a%") DO set typ=%%T 
for /F "tokens=1 delims=_" %%P IN ("%a%") DO set prefix=%%P 
cd /d %1
REM @echo 'which maven do you want? isbank or public'
REM @SET /P x=[mvntype]
@REM IF %x%==isbank call "C:\apache-maven-3.3.9\bin\mvn" clean install -DskipTests
REM @IF %x%==isbank call "C:\apache-maven-3.3.9\bin\mvn" clean install
REM @IF %x%==public call "C:\apache-maven-3.3.9\bin\mvn" -o -s "C:\apache-maven-3.3.9\conf\settings.xml" clean install
REM call "C:\JAVA\apache-maven-3.6.3\bin\mvn" -s "C:\Users\CY59857\.m2\settings_isbank.xml" clean install
@set JAVA_HOME = C:\JAVA\jdk1.8.0_261
set JAVA_HOME=C:\Java\jdk-11.0.11
setx JAVA_HOME "%JAVA_HOME%" /M
set Path=%JAVA_HOME%\bin;%Path%
REM call "C:\JAVA\apache-maven-3.6.3\bin\mvn" compile assembly:single
call "C:\JAVA\apache-maven-3.6.3\bin\mvn" clean install

pause
