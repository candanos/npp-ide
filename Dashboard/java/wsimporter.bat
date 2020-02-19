set JRE_HOME="C:\JAVA\jdk1.8.0_181"
set JRE_HOME="C:\JAVA\jdk1.8.0_181\jre"
set generationDir="C:\projects\footballStats\footballStatsWeb\src\main\java"
call wsimport -Xnocompile -keep -s %generationDir% http://localhost:8080/footballStatsWeb/football?wsdl 
pause