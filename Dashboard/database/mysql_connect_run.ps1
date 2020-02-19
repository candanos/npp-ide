#Set-ExecutionPolicy -Scope CurrentUser
#connect the library MySql.Data.dll
Add-Type –Path "C:\Program Files (x86)\MySQL\Connector NET 8.0\Assemblies\v4.5.2\MySql.Data.dll"
# database connection string, server — server name, uid - mysql user name, pwd- password, database — name of the database on the server
$Connection = New-Object MySql.Data.MySqlClient.MySqlConnection
$Connection.ConnectionString = "server=127.0.0.1;uid=root;pwd=xxxx;database=eclub"
$Connection.Open()
$sql = New-Object MySql.Data.MySqlClient.MySqlCommand
$sql.Connection = $Connection
$sql.CommandText = `
"create table ECLUB_PLAYER_TEAM_LINK (PLAYER_ID int, TEAM_ID int); " + `
"create table ECLUB_ECLUB (ID int, CLUB_NAME varchar(50));"
"create table ECLUB_TEAM (ID int, TEAM_NAME varchar(100), LEAGUE int, GROUP_NAME varchar(15), LEVEL int, MANAGER_ID int, HEAD_COACH_ID int, LEAGUE_TEAM_ID int); " + `
"create table ECLUB_PARENT_CHILD_LINK (CHILD_ID int, PARENT_ID int); " + `
"create table ECLUB_INDIVIDUAL (ID int, FIRST_NAME varchar(50), LAST_NAME varchar(50), EMAIL varchar(50), LOGIN varchar(50)); " + ` 
"create table ECLUB_PLAYER (ID int, JERSEY_NO int, POSITION varchar(15), DOB date); " + `
"create table ECLUB_COACH (ID int, CERT_NO int, CERT_LEVEL int); " + `
"create table ECLUB_TEAM (ID int, TEAM_NAME varchar(100), LEAGUE int, GROUP_NAME varchar(15), LEVEL int, MANAGER_ID int, HEAD_COACH_ID int, LEAGUE_TEAM_ID int); " + `
"create table ECLUB_PLAYER_TEAM_LINK (PLAYER_ID int, TEAM_ID int); " + `
"create table ECLUB_ECLUB (ID int, CLUB_NAME varchar(50));"
$sql.ExecuteNonQuery()
$Connection.Close()

#GRANT SELECT ON *.* TO 'username'@'localhost';
#GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';
#CREATE DATABASE dbname;
#USE dbname;
#CREATE TABLE tablename ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );
#INSERT INTO tablename ( id, name ) VALUES ( null, 'Sample data' );
