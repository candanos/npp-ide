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
$repopath = "C:\JAVA\repositories\javax.jws-3.1.1.jar;C:\JAVA\repositories\jaxws-api-2.3.1.jar;C:\JAVA\repositories\ibmjzos.jar" 

$sourcepath = $filePath
Set-Location $filePath #prjPath/src/package
Set-Location ..  #prjPath/src/
Set-Location ..	 #prjPath

$prjPathInfo = Get-Location
$prjPath = $prjPathInfo.ToString() 
$classpath = $prjPath + "\target;" + $repopath 
$targetpath = $prjPath + "\target"

Write-Host("sourcepath: " + $sourcepath)
Write-Host("classpath : " + $classpath)
Write-Host("targetpath: " + $targetpath)

Set-Location $filePath
javac -d $targetpath -sourcepath $sourcepath -cp $classpath $fileName
