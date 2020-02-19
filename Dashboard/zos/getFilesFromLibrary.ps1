#bright profiles update zosmf-profile vsc --password o5o5o5o5

bright zos-files download all-members -e .cbl CY59857.IMSDECOM.SOURCE -d "C:\Users\CY59857\Desktop\imsdecom\src" 

$dirName = "C:\zos-cobol\imsdecom\src"
$Filenames = Get-ChildItem $dirName 

Foreach ($file in $Filenames) {
	Write-Host ($file)
}
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

# bright zos-tso issue command "EXEC 'CY59857.TOOLS.REXX(STARTISP)'" --ssm

# bright zos-files upload dir-to-pds

        # Upload files from a local directory to a partitioned data set (PDS)

# bright zos-files upload dir-to-uss

        # Upload a local directory to a USS directory

# bright zos-files upload file-to-data-set

        # Upload the contents of a file to a z/OS data set

# bright zos-files upload file-to-uss

        # Upload content to a USS file from local file

# bright zos-files upload stdin-to-data-set

        # Upload the content of a stdin to a z/OS data set
		
		
		