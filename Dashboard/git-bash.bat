@REM To run with: git-bash $(CURRENT_DIRECTORY) $(FILE_NAME)
cd %1
Call "C:\Program Files\Git\git-bash.exe"
pause
read -p "Press enter to continue"
exit