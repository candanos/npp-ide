#Set-ExecutionPolicy -Scope CurrentUser
#connect the library MySql.Data.dll
Add-Type -Path "C:\Program Files (x86)\MySQL\Connector NET 8.0\Assemblies\v4.5.2\MySql.Data.dll"
# database connection string, server — server name, uid - mysql user name, pwd- password, database — name of the database on the server
$Connection = New-Object MySql.Data.MySqlClient.MySqlConnection
$Connection.ConnectionString = "server=127.0.0.1;uid=root;pwd=xxxx;database=dbIsbankTest"
$Connection.Open()
$sql = New-Object MySql.Data.MySqlClient.MySqlCommand
$sql.Connection = $Connection
$sql.CommandText = `
"create table tbhesap (ID int, account_id int, account_typ char(3));"
$sql.ExecuteNonQuery()
$Connection.Close()