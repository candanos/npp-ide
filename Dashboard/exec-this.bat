@REM save command as > "C:\Cloud\OneDrive - candanos\Master\Dashboard\exec-this.bat" "$(CURRENT_DIRECTORY)" $(FILE_NAME)  
@echo off
@set dashboard=C:\Cloud\OneDrive - candanos\Master\Dashboard
@set gitlabPrj=C:\Cloud\CodeRepos\gitlab
@set gitPath=C:\Program Files\Git
@set pythonPath=C:\Python38
@set nodePath=C:\nodejs"
@set batchPath=C:\WINDOWS\System32
@set powerShPath="C:\Windows\System32\WindowsPowerShell\v1.0"
@set vbsPath="C:\WINDOWS\System32"
@set a=%2
for /F "tokens=1 delims=." %%N IN ("%a%") DO set name=%%N  
for /F "tokens=2 delims=." %%T IN ("%a%") DO set typ=%%T 
for /F "tokens=1 delims=_" %%P IN ("%a%") DO set prefix=%%P 
cd /d %1
@REM bat files
IF %typ%==bat %batchPath%\cmd.exe /c %2
@REM vbs files
IF %typ%==vbs %vbsPath%"\cscript.exe" %2
@REM ps1 files
IF %typ%==ps1 %powerShPath%"\powershell.exe" -File %2
@REM poms
IF %typ%==xml ( IF %name%==pom ( call "%dashboard%\java\pom.bat" %1 %2 ))
@REM java builds
IF %typ%==java "%dashboard%\java\JavaCompile.bat" %1 %2
@REM js
IF %typ%==js %nodePath%"\node" %2
@REM py
IF %typ%==py %pythonPath%"\python.exe" %2
@REM IF %typ%==sh
IF %typ%==sh call %gitPath%"\git-bash.exe"  %2     
@REM ServiceRequests
IF %prefix%==request %powerShPath%"\powershell.exe" "%dashboard%\network\SendRequest.ps1" -filePath %1 -requestFl %2 -type %typ%
@REM Sql Queries
IF %typ%==sql ( IF %prefix%==verim ( %powerShPath%"\powershell.exe" "%dashboard%\database\verimInquiry.ps1" %1 %2 ) )
IF %typ%==sql ( IF %prefix%==borclure ( %powerShPath%"\powershell.exe" "%gitlabPrj%\imsdecom\mutabakat\borclure\sqlRunner.ps1" %1 %2 ) )
IF %typ%==sql ( IF %prefix%==pp ( %powerShPath%"\powershell.exe"  "%gitlabPrj%\imsdecom\mutabakat\payment_plan\sqlRunner.ps1" %1 %2 ) )
IF %typ%==sql ( IF %prefix%==fybs ( %powerShPath%"\powershell.exe"  "%gitlabPrj%\imsdecom\mutabakat\fybs\sqlRunner.ps1" %1 %2 ) )
pause
exit