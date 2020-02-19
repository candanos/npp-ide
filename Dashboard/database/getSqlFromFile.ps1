param (  
    [string]$sqlFl = $(throw "-sqlFl is required."),
	[string]$filePath = $(throw "-filePath is required."),

$fullname = filePath + "/" + sqlFl
$dummyFl = "dummy.sql"
(Get-Content $requestFL).replace('\n', ' ') | Set-Content $dummyFl
$sqlDataArr=($requestFl -split ";")
$sqlStr=$sqlDataArr[0]
	