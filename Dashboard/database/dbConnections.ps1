Add-Type -Path "C:\oracle\product\12.2.0\client_1\ODP.NET\managed\common\Oracle.ManagedDataAccess.dll"
#$connection = New-Object Oracle.ManagedDataAccess.Client.OracleConnection("User Id=59857;Password=Cy232323;Data Source=server.domain.com:PORT/DBINSTANCE")
$connection = New-Object Oracle.ManagedDataAccess.Client.OracleConnection("User Id=59857;Password=Cy232323;Data Source=VERIMPRD_DDMA")
$connection.open()