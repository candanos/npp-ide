# To run with: JavaCompile $(CURRENT_DIRECTORY) $(FILE_NAME)
# You can add classpath maven dependencies, and projects other folders. So you can
# compile any class.
# echo off

param (  
	[string]$filePath = $(throw "-filePath is required."),
    [string]$fileName = $(throw "-sqlFl is required.")
	)

# $env:Path = "C:\JAVA\jdk-14.0.1\bin;" + $env:Path
$env:Path = "C:\JAVA\jdk1.8.0_241\bin;" + $env:Path

Set-Location $filePath #prjPath/src/package
Set-Location ..  #prjPath/src/
Set-Location ..	 #prjPath
$prjPathInfo = Get-Location
$prjPath = $prjPathInfo.ToString() 
$classpath = $prjPath + "\target"

Get-ChildItem  "C:\JAVA\repositories" | 
Foreach-Object {
	$classpath = $classpath + ";" + $_.FullName
}


$sourcepath = $filePath
$targetpath = $prjPath + "\target"

Write-Host("sourcepath: " + $sourcepath)
Write-Host("classpath : " + $classpath)
Write-Host("targetpath: " + $targetpath)

Set-Location $filePath
javac -d $targetpath -sourcepath $sourcepath -cp $classpath $fileName
