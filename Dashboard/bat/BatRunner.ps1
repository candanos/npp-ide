# If you want to capture the output of the .bat file, you can use:

# $out = C:Pathfile.bat

# If you want to start a process with your .bat file, you can use the PowerShell start-process cmdlet:

# start-process C:Pathfile.bat

# And, if you if you want to control cmd.exe, you can use this:

# start-process "cmd.exe" "/c C:Pathfile.bat"

param (  
	[string]$filePath = $(throw "-filePath is required."),
    [string]$fileName = $(throw "-sqlFl is required.")
	)
	
$env:Path = "C:\JAVA\apache-maven-3.6.3\bin;" + $env:Path

$batPath = $filePath + "\" + $fileName
start-process $batPath