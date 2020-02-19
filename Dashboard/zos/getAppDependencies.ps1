#bright profiles update zosmf-profile vsc --password o5o5o5o5


$dirName = "C:\code-workspaces\batchbor"
# bright zos-files download all-members -e .cpy 'SBCOMMON.PROD.COPY' -d $dirName  

Function Get-Dependencies
{
Param(
    [Parameter(Mandatory=$true)]
    [string]$moduleName
)
   # Source File with connection variables set
<# 	$Path = $PSScriptRoot
. "$Path\db2_dev_variables.ps1" #>

	#Define connection string for the database
	$db2ConnStr = "Provider=ibmdadb2;Driver={IBM DB2 ODBC DRIVER - DB2COPY1};Database=DV0BPLOC;Hostname=dv0bdb2.isbank;Port=446;Protocol=TCPIP;Uid=CY59857;Pwd=o5o5o5o5"
	$cn = new-object system.data.OleDb.OleDbConnection($db2ConnStr);
	#Define data set for first query
	$ds = new-object "System.Data.DataSet" "ds"
	#Define query to run
	$q = "SELECT PGMNAME, PRJNAME, 'COPY' FROM SCDEGISK.MODULS WHERE PGMNAME IN (SELECT DISTINCT COPYNAME FROM SCDEGISK.CPYFIELD WHERE PROGNAME IN (select program2 from scdegisk.pgmdrive where program1 = 'BATCHBOR')) UNION SELECT PGMNAME, PRJNAME, 'COBOL' FROM SCDEGISK.MODULS WHERE PGMNAME IN (select program2 from scdegisk.pgmdrive where program1 = 'BATCHBOR')"
	# Define data object given the specific query and connection string
	$da = new-object "System.Data.OleDb.OleDbDataAdapter" ($q, $cn)
	# Fill the data set - essentially run the query. 
	$da.Fill($ds)
	# Print the result

	foreach($table in $ds.Tables)
    {
        foreach($row in $table.Rows)
        {
            Write-Host("new row:" + $row[0] + ";" + $row[1] + ";" + $row[2]) 
			$mbr=$row[0].trim()
			$prj=$row[1].trim()
			$typ=$row[2].trim()
			$sourceFile=$prj + ".PROD." + $typ + "(" + $mbr + ")" 
			Write-Host($sourceFile)
			foreach ($column in $table.Columns)
            {
                Write-Host($row[$column])
            }
			if($typ="COBOL") {
				$destFile=$dirName + "\" + $mbr + ".cbl"
				bright zos-files download data-set -e .cbl $sourceFile
			} else {
				$destFile=$dirName + "\" + $mbr + ".cpy"
				bright zos-files download data-set -e .cpy $sourceFile
			}
		}
}	

	
	# Close the Connection
	$cn.close()
	Write-Host("Here.")
	return ,$ds
}
 
Get-Dependencies $dirName
 

<# 
Function Remove-LineNumbers
{
Param(
    [Parameter(Mandatory=$true)]
    [string]$dirName
)
   $Filenames = Get-ChildItem $dirName 
   Foreach ($file in $Filenames) {
	$srcfile = $dirName + "\" + $file
	Write-Host ($srcfile)
 	$oldContent = Get-Content $srcfile
	$newContent = $OldContent | 
	ForEach-Object { 
		$len = $_.length
		if($len -gt 79) {
			"      " + $_.substring(6,66) + "        "
		}else {
			$_
		}
	}	
	$newContent | Set-Content $srcfile 
 }
}
 #>