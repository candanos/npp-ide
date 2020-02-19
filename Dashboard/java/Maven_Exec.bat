@REM To run with: JavaRun $(CURRENT_DIRECTORY) $(NAME_PART)
@echo off
@cd /d %1
@For /F "tokens=1" %%I in ('cd') Do Set prjPath=%%I
@echo first prjPath=%prjPath%
@cd /d %1
set a=%2
echo a=%a%
For /F "tokens=1 delims=." %%N IN ("%a%") DO set mainclass=%%N
@SET mainclass=com.candanos.%mainclass%
call "C:\apache-maven-3.3.9\bin\mvn" -s "C:\apache-maven-3.3.9\conf\settings_local.xml" exec:java -Dexec.mainClass=%mainClass% [-Dexec.args="arg1"]
pause