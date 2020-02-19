#Set-ExecutionPolicy -Scope CurrentUser
#connect the library MySql.Data.dll
Add-Type –Path "C:\Program Files (x86)\MySQL\Connector NET 8.0\Assemblies\v4.5.2\MySql.Data.dll"
# database connection string, server — server name, uid - mysql user name, pwd- password, database — name of the database on the server
$Connection = New-Object MySql.Data.MySqlClient.MySqlConnection
$Connection.ConnectionString = 'server=127.0.0.1;uid=root;pwd=xxxx;database=dbeurofootball'
$Connection.Close()
$Connection.Open()
$sql = New-Object MySql.Data.MySqlClient.MySqlCommand
Write-Output($sqlStr)
$sql.Connection = $Connection
$sqlStr = "ALTER TABLE tbmatch CHANGE COLUMN mID mID INT(11) NOT NULL;"
$sqlStr = "ALTER TABLE tbmatch CHANGE COLUMN mID mID INT(11) NOT NULL, ADD UNIQUE INDEX mID_UNIQUE (mID ASC) VISIBLE, ADD PRIMARY KEY (mID), ADD INDEX tbmatch_IDX_1 (mTmId ASC) VISIBLE;"
Write-Output($sqlStr)
$sql.CommandText = $sqlStr
$sql.ExecuteNonQuery()
$Connection.Close()