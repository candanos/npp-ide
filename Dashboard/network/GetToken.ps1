if($level -eq "prod") {
	$snoopEndpoint="https://klaccwas01.isbank:9443/snoop"
	
	#Authorizations
	#$cred = Get-Credential
	$user = '59857'
	$pass = 'Os131313'
	$pair = "$($user):$($pass)"
	$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
	$basicAuthValue = "Basic $encodedCreds"
	$Headers = @{
		Authorization = $basicAuthValue
}
	
#Bypass Certificates
add-type @"
	using System.Net;
	using System.Security.Cryptography.X509Certificates;
	public class TrustAllCertsPolicy : ICertificatePolicy {
		public bool CheckValidationResult(
			ServicePoint srvPoint, X509Certificate certificate,
			WebRequest request, int certificateProblem) {
			return true;
		}
	}
"@
[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy
#Bypass Certificates
	
	$result=Invoke-WebRequest -Uri $SnoopEndpoint -Headers $Headers
	
#ExtractToken
	$tokenArr1=($result.rawcontent -split "LtpaToken=")
	$tokenStr=$tokenArr1[1]
	$tokenArr2=($tokenStr -split "; Path=/;")
	$token=$tokenArr2[0]
}

if($level -eq "uat" -Or $level -eq "int" -Or $level -eq "dev" ) {
	if($level -eq "uat") {
		$tokenRequestFL="C:\Dashboard\isbank\serviceRequests\request_uat_Token_Generator.xml"
		$endpnt="http://eaesbgatewayuat.gm.isbank.com.tr:7996/WSSec2LTPA"
	}
	if($level -eq "int" -Or $level -eq "dev" ) {
		$tokenRequestFL="C:\Dashboard\isbank\serviceRequests\request_int_Token_Generator.xml"
		$endpnt="http://eaesbgatewaysit.gm.isbank.com.tr:7996/WSSec2LTPA"
	}
	$tokenResponseFl="C:\Dashboard\isbank\serviceRequests\responsex.xml"	
	Write-Host ("tokenRequestFL:" + $tokenRequestFL)
	
	Invoke-WebRequest $endpnt -Method 'POST' -ContentType "text/xml" -InFile $tokenRequestFL -OutFile $tokenResponseFl
	
	$raw = Get-Content -Path $tokenResponseFl -Raw
	
	Write-Host ("tokenResp:" + $raw)
		
	$delimiter1='http://www.ibm.com/websphere/appserver/tokentype/5.0.2">'
	$delimiter2='</wsse:BinarySecurityToken>'
	
	$tokenArr1=($raw -split $delimiter1)
	$tokenStr=$tokenArr1[1]
	$tokenArr2=($tokenStr -split $delimiter2)
	$token=$tokenArr2[0]
	Write-Host ("token:" + $token)
}
