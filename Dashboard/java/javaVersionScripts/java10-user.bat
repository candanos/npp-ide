@echo off
set JAVA_HOME=C:\Program Files\Java\jdk-10.0.2
setx JAVA_HOME "%JAVA_HOME%"
set Path=%JAVA_HOME%\bin;%Path%
echo Java 10 activated as user default.
