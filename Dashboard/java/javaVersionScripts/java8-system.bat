@echo off
set JAVA_HOME=C:\Java\jdk1.8.0_261
setx JAVA_HOME "%JAVA_HOME%" /M
set Path=%JAVA_HOME%\bin;%Path%
echo Java 8 activated as system-wide default.
pause