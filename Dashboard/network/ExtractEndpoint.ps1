if(($type -eq "json")) { 
	foreach($line in Get-Content $requestFl) {
		if($line -like '#endpoint#*#endpoint#'){
			$endpointArr=($line -split "#endpoint#")
			$endpoint=$endpointArr[1]
			Write-Host ("endpoint json:" + $endpoint)
		}else{
			$request=$request + " " + $line		
		}
	} 
}

if(($type -eq "xml")) { 
	foreach($line in Get-Content $requestFl) {
		if($line -like '*#endpoint#*#endpoint#*'){
			$endpointArr=($line -split "#endpoint#")
			$endpoint=$endpointArr[1]
			Write-Host ("endpoint xml:" + $endpoint)
		}		
	}
} 
