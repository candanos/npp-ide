REM set JRE_HOME="C:\Java\jdk-9.0.4"
REM set JRE_HOME="C:\Java\jdk1.8.0_261\jre"
REM set JRE_HOME="C:\Java\jdk-11.0.11"
REM set JAVA_HOME="C:\Java\jdk-11.0.11"

REM @echo off
set JAVA_HOME=C:\Java\jdk1.8.0_261
set JAVA_HOME=C:\Java\jdk-11.0.11
setx JAVA_HOME "%JAVA_HOME%" /M
set Path=%JAVA_HOME%\bin;%Path%
REM echo Java 11 activated as system-wide default.

echo %JRE_HOME%
cd "C:\JAVA\servers\apache-tomcat-9.0.37\bin"
cd "C:\JAVA\servers\apache-tomee-webprofile-9.0.0-M7\bin"
call startup