set JAVA_HOME="C:\java\jdk-17.0.9"
export %JAVA_HOME% 
set Path=%JAVA_HOME%\bin;%Path%
set activeMQ_Home="C:\java\middleware\windows\apache-activemq-6.1.3"
cd %activeMQ_Home%"\bin"
activemq.bat stop
REM activemq.bat start

REM start firefox "http://localhost:8161/admin"
REM url:
REM http://localhost:8161/admin
REM user:admin
REM password:admin
