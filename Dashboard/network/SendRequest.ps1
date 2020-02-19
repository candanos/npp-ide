# To run with: SendRequest.ps1 $(FILE_NAME) $(PATH_OF_FILE)  $(TYPE)
param (  
    [string]$requestFl = $(throw "-requestFl is required."),
	[string]$filePath = $(throw "-filePath is required."),
	[string]$type = $(throw "-type is required.")
)
Write-Host ("type:" + $type)
Write-Host ("requestFl:" + $requestFl)
Write-Host ("filePath:" + $filePath)
cd ($filePath)
$errorFL="error.xml"
$responseFl="response.xml"
$dummyFl="req.xml"
$reqDataArr=($requestFl -split "_")
$level=$reqDataArr[1]

. 'C:\Dashboard\network\ExtractEndpoint.ps1'
. 'C:\Dashboard\network\GetToken.ps1'

(Get-Content $requestFL).replace('LtpaToken', $token) | Set-Content $dummyFl -Encoding UTF8

Invoke-WebRequest $endpoint -Method 'POST' -ContentType "text/xml;charset=UTF-8" -InFile $dummyFL 2>$error -OutFile $responseFl
	
& "C:\Program Files (x86)\Notepad++\notepad++.exe" $responseFl
		
if($error) {
	Write-Output($error) > $errorFL	
	& "C:\Program Files (x86)\Notepad++\notepad++.exe" $errorFL
}
 