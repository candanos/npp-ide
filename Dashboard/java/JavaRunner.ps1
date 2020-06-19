# To run with: JavaCompile $(CURRENT_DIRECTORY) $(FILE_NAME)
# You can add classpath maven dependencies, and projects other folders. So you can
# compile any class.
# echo off

param (  
	[string]$filePath = $(throw "-filePath is required."),
    [string]$fileName = $(throw "-sqlFl is required.")
	)

$env:Path += ";C:\JAVA\jdk-14.0.1\bin"
$repopath = "C:\JAVA\repositories\javax.jws-3.1.1.jar;C:\JAVA\repositories\jaxws-api-2.3.1.jar" 

Set-Location $filePath
Set-Location ..
$prjPathInfo = Get-Location
$prjPath = $prjPathInfo.ToString() 
$classpath = $prjPath + "\target;" + $repopath 
$mainclassPath = $filePath + "\" + $fileName 

foreach($line in Get-Content $mainclassPath) {
		if($line -like '*<mainclass>*</mainclass>*'){
			$javamainArr=($line -split "<mainclass>")
			$mainclassArr=($javamainArr[1] -split "<")
			$mainclass = $mainclassArr[0]
			Write-Host ("mainclass:" + $mainclass)
		}		
	}

Write-Host("classpath : " + $classpath)

# Set-Location $filePath
java -cp $classpath $mainclass -v 
