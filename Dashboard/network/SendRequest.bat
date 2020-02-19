@REM To run with: exec-this.bat $(CURRENT_DIRECTORY) $(FILE_NAME)
echo off
cd %1
@set a=%2 
for /F "tokens=1 delims=." %%N IN ("%a%") DO set name=%%N
for /F "tokens=2 delims=." %%T IN ("%a%") DO set typ=%%T
for /F "tokens=1 delims=_" %%P IN ("%a%") DO set prefix=%%P
set requestFl=%2
pause
For /F "tokens=2 delims=#endpoint#" %%G in (%requestFl%) DO set endpoint=%%G
echo %endpoint% 
If typ=json set contentType="Content-Type: application/json"
If typ=xml set contentType="Content-Type: text/xml;charset=UTF-8"
call "C:\Tools\curl-7.64.0-win64-mingw\bin\curl.exe" -H %contentType% -d @%requestFl% %endpoint%
pause