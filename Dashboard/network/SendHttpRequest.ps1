$request="SendingRequest"
$endpoint="https://klaccwas01.isbank:9443/snoop"
Write-Host ("Invoking WebRequest")
#Authorizations
#$cred = Get-Credential
$user = '59857'
$pass = 'cD194775'
$pair = "$($user):$($pass)"
$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
$basicAuthValue = "Basic $encodedCreds"
$Headers = @{
    Authorization = $basicAuthValue
}
#ByPassCertificates
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
#ByPassCertificates

$result=Invoke-WebRequest -Uri $endpoint -Headers $Headers

#ExtractToken
$tokenArr1=($result.rawcontent -split "LtpaToken=")
$tokenStr=$tokenArr1[1]
$tokenArr2=($tokenStr -split "; Path=/;")
$token=$tokenArr2[0]