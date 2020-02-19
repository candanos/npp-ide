@REM To run with: JavaRun $(CURRENT_DIRECTORY) $(NAME_PART)
@echo off
@cd /d %1
@cd..
@For /F "Tokens=1" %%I in ('cd') Do Set prjPath=%%I
set a=%2
For /F "tokens=1 delims=." %%N IN ("%a%") DO set mainclass=%%N
@set mainclass=%mainclass%
@set sourcepath=%prjPath%\src
@set classpath=%sourcepath%;%prjPath%\target;C:\JAVA\repository
echo prjpath=%prjPath%
echo classpath=%classpath%
echo mainclass=%mainclass%
java -cp %classpath% %mainclass% -v 
@pause
REM @For /F "tokens=1,2,3,4,5 delims=\" %%N IN ("%prjPath%") DO set mvnmainproj=%%N\%%O\%%P
REM @echo mvnmainproj=%mvnmainproj%
REM @For /F "tokens=1,2,3,4,5 delims=\" %%N IN ("%prjPath%") DO set mvnsubproj=%%N\%%O\%%P\%%Q
REM @echo mvnsubproj=%mvnsubproj%