cd C:\JAVA\servers\glassfish4\glassfish\bin

REM set JRE_HOME="C:\Java\jdk1.7.0_80\jre"
REM glassfish4 works only with Java 7
set AS_JAVA="C:\Java\jdk1.8.0_261"
set AS_JAVA="C:\Java\jdk1.7.0_80"
call asadmin start-domain
pause