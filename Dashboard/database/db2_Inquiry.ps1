param (  
	[string]$filePath = $(throw "-filePath is required."),
    [string]$sqlFl = $(throw "-sqlFl is required.")
	)
Write-Output(Get-Date -Format g)
function Get-DataTable 
{
Param(
    [Parameter(Mandatory=$true)]
    [Oracle.ManagedDataAccess.Client.OracleConnection]$conn, 
    [Parameter(Mandatory=$true)]
    [string]$sql
)
    $cmd = New-Object Oracle.ManagedDataAccess.Client.OracleCommand($sql,$conn)
    $da = New-Object Oracle.ManagedDataAccess.Client.OracleDataAdapter($cmd)
    $dt = New-Object System.Data.DataTable
    [void]$da.Fill($dt) 
    return ,$dt
}
Add-Type -Path "C:\oracle12\64bit\client\CY59857\product\12.2.0\client_1\ODP.NET\managed\common\Oracle.ManagedDataAccess.dll"
$sqlfilename = $filePath + "/" + $sqlFl
$sqlString = (Get-Content -Path $sqlfilename -Raw).replace('\n', ' ')
$sqlDataArr=($sqlString -split ";")
$sqlStr=$sqlDataArr[0]
Write-Output($sqlStr)	
$fileNameArr=($sqlfilename -split "verim_")
$fileName=$fileNameArr[1]
Write-Output($fileName)
$connection = New-Object Oracle.ManagedDataAccess.Client.OracleConnection("User Id=59857;Password=Os131313;Data Source=VERIMPRD_DDMA")
$connection.open()
$dt = Get-DataTable $connection $sqlStr
$connection.Close()
Write-Output("completed.")
$path = "C:\Users\CY59857\Desktop\"
$resultFile = $path + $fileName
$resultFile = $resultFile.replace(".sql", ".csv")
Write-Output($resultFile)
$dt | Export-CSV $resultFile -Delimiter ";"

Write-Output(Get-Date -Format g)

