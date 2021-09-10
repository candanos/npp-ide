@REM save command as > "C:\Cloud\github\npp-ide\Dashboard\exec-this.bat" "$(CURRENT_DIRECTORY)" $(FILE_NAME)  
@echo off
@set dashboard=C:\Cloud\github\npp-ide\Dashboard
@set gitlabPrj=C:\Cloud\CodeRepos\gitlab
@set gitPath=C:\Program Files\Git
@set pythonPath=C:\Python
@set nodePath=C:\nodejs
@set batchPath=C:\WINDOWS\System32
@set powerShPath="C:\Windows\System32\WindowsPowerShell\v1.0"
@set vbsPath="C:\WINDOWS\System32"
@set a=%2
for /F "tokens=1 delims=." %%N IN ("%a%") DO set name=%%N  
for /F "tokens=2 delims=." %%T IN ("%a%") DO set typ=%%T 
for /F "tokens=1 delims=_" %%P IN ("%a%") DO set prefix=%%P 
cd /d %1
@REM bat files
@REM IF %typ%==bat start %powerShPath%"\powershell.exe" -File "%dashboard%\bat\batRunner.ps1" %1 %2
IF %typ%==bat start powershell -File "%dashboard%\bat\batRunner.ps1" %1 %2
@REM IF %typ%==bat %batchPath%"\cmd.exe" "/C "  %2
@REM vbs files
IF %typ%==vbs %vbsPath%"\cscript.exe" %2
@REM ps1 files
IF %typ%==ps1 %powerShPath%"\powershell.exe" -File %2
@REM poms
IF %typ%==xml ( IF %name%==pom ( call "%dashboard%\java\pom.bat" %1 %2 ))
@REM java runner
IF %typ%==xml ( IF %name%==javamain ( %powerShPath%"\powershell.exe" -File "%dashboard%\java\JavaRunner.ps1" %1 %2 ))
@REM java builds
IF %typ%==java %powerShPath%"\powershell.exe" -File "%dashboard%\java\JavaCompile.ps1" %1 %2
@REM js
IF %typ%==js %nodePath%"\node" %2
@REM py
IF %typ%==py %pythonPath%"\python.exe" %2
@REM IF %typ%==sh
IF %typ%==sh call "%gitPath%""\git-bash.exe"  %2     
@REM ServiceRequests
IF %prefix%==request %powerShPath%"\powershell.exe" "%dashboard%\network\SendRequest.ps1" -filePath %1 -requestFl %2 -type %typ%
@REM Sql Queries
IF %typ%==sql  %pythonPath%"\python.exe"  "%dashboard%\database\sqlRunner.py" %1 %2 
pause
exit