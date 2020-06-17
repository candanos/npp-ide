# To run with: JavaCompile $(CURRENT_DIRECTORY) $(FILE_NAME)
# You can add classpath maven dependencies, and projects other folders. So you can
# compile any class.
# echo off

param (  
	[string]$filePath = $(throw "-filePath is required."),
    [string]$fileName = $(throw "-sqlFl is required.")
	)
$sourcepath = $filePath
Set-Location $filePath
Set-Location ..
$prjPathInfo = Get-Location
$prjPath = $prjPathInfo.ToString() 
$classpath = $prjPath + "\target;C:\JAVA\repository"
$targetpath = $prjPath + "\target"
Set-Location $filePath
javac -d $targetpath -sourcepath $sourcepath -cp $classpath $fileName
