@REM To run with: JavaCompile $(CURRENT_DIRECTORY) $(FILE_NAME)
@REM You can add classpath maven dependencies, and projects other folders. So you can
@REM compile any class.
@REM echo off
@cd /d %1
@cd..
@For /F "Tokens=1" %%I in ('cd') Do Set prjPath=%%I
echo prjpath=%prjPath%
@cd /d %1
@set sourcepath=%1
echo sourcepath=%sourcepath% 
@set classpath=%prjPath%\target;C:\JAVA\repository
echo classpath=%classpath%
@set targetpath=%prjpath%\target
javac -d %targetpath% -sourcepath %sourcepath% -cp %classpath% %2
@pause