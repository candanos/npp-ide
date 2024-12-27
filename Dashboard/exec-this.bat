@REM save command as > C:\npp-ide\Dashboard\exec-this.bat "$(CURRENT_DIRECTORY)" $(FILE_NAME)
@echo off
@set dashboard=C:\npp-ide\Dashboard
@set gitlabPrj=C:\Cloud\CodeRepos\gitlab
@set gitPath=C:\Program Files\Git
@set PYTHONPATH=C:\python\Python313
@set PIPPATH=%PYTHONPATH%\Scripts
@set nodePath=C:\nodejs
@set batchPath=C:\WINDOWS\System32
@set powerShPath="C:\Windows\System32\WindowsPowerShell\v1.0"
@set vbsPath="C:\WINDOWS\System32"
@set CYGWIN_PATH=C:\cygwin64\bin
@set bashPath="C:\cygwin64\bin"
@set makePath="C:\cygwin64\bin"
@set PATH=%PIPPATH%;%PYTHONPATH%;%PATH%

@set a=%2
cd /d %1

for /F "tokens=1 delims=." %%N IN ("%a%") DO set name=%%N  
for /F "tokens=2 delims=." %%T IN ("%a%") DO set typ=%%T 
for /F "tokens=1 delims=_" %%P IN ("%a%") DO set prefix=%%P 

FOR /F "tokens=* USEBACKQ" %%F IN (`"%CYGWIN_PATH%\cygpath.exe %1%"`) DO (
SET UNIX_PATH=%%F
)
REM echo "exec-this UNIX_PATH:"
REM echo %UNIX_PATH%

REM echo "exec-this WINDOWS_PATH:"
REM cd

@REM bat files
@REM IF %typ%==bat start %powerShPath%"\powershell.exe" -File "%dashboard%\bat\batRunner.ps1" %1 %2
REM IF %typ%==bat start powershell -File "%dashboard%\bat\batRunner.ps1" %1 %2"

IF %typ%==bat %batchPath%"\cmd.exe" "/C "  %2
@REM vbs files
IF %typ%==vbs %vbsPath%"\cscript.exe" %2
@REM ps1 files
IF %typ%==ps1 %powerShPath%"\powershell.exe" -File %2
@REM poms
IF %typ%==xml ( IF %name%==pom ( call "%dashboard%\java\pom.bat" %1 %2 ))
@REM java runner
IF %typ%==xml ( IF %name%==javamain ( %powerShPath%"\powershell.exe" -File "%dashboard%\java\JavaRunner.ps1" %1 %2 ))
@REM java builds
REM IF %typ%==java %powerShPath%"\powershell.exe" -File "%dashboard%\java\JavaCompile.ps1" %1 %2
REM IF %typ%==java %pythonPath%"\python.exe" "%dashboard%\java\JavaCompile.py" %1 %2
IF %typ%==java "%bashPath%""\bash.exe" "%dashboard%\java\java_go.sh" %1 %2
@REM js
IF %typ%==js %nodePath%"\node" %2
@REM py
IF %typ%==py %PYTHONPATH%"\python.exe" %2
@REM sh
IF %typ%==sh %bashPath%"\bash.exe" %2 "prm1" "prm2"
REM IF %typ%==sh %bashPath%"\bash.exe" -c "cd %UNIX_PATH% && chmod +x %2 && %UNIX_PATH%'/'%2 %UNIX_PATH% %2"
REM IF %typ%==sh call "%gitPath%""\git-bash.exe" %2
@REM ServiceRequests
IF %prefix%==request %powerShPath%"\powershell.exe" "%dashboard%\network\SendRequest.ps1" -filePath %1 -requestFl %2 -type %typ%
@REM Sql Queries
IF %typ%==sql  %PYTHONPATH%"\python.exe"  "%dashboard%\database\sqlRunner.py" %1 %2
@REM toml
IF %typ%==toml ( IF %name%==pyproject ( call "%dashboard%\ide\pycharm.bat" %1 %2 ))
@REM ipynb (jupyter notebook)
IF %typ%==ipynb "%bashPath%""\bash.exe" "%dashboard%\jupyter\start_jupyter.sh" %1 %2
@REM md (render markdown files)
IF %typ%==md %PYTHONPATH%"\python.exe"  "%dashboard%\md\md_renderer.py" %1 %2
pause
exit