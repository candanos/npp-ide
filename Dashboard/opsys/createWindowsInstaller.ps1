Write-Verbose "Setting Arguments" -Verbose
$StartDTM = (Get-Date)
$Vendor = "Microsoft"
$Product = "Visual Studio Code"
$Version = "1.37.0"
$PackageName = "VSCodeUserSetup-x64-1.37.0"
$InstallerType = "exe"
$Source = "C:\Users\CY59857\Desktop\vscode_zowe_node"
$LogPS = $Source + "\Temp\$Vendor $Product $Version PS Wrapper.log"
$LogApp = $Source + "\Temp\$PackageName.log"
$UnattendedArgs = '/verysilent /suppressmsgboxes /SAVEINF="VSCodeSetup-ia32-1.18.1.ini" /Dir="C:\Microsoft VS Code"   /mergetasks=!runcode,addcontextmenufiles,addcontextmenufolders,associatewithfiles,addtopath'
$ProgressPreference = 'SilentlyContinue'
Start-Transcript $LogPS
CD $Source
Write-Verbose "Starting Installation of $Vendor $Product $Version"
(Start-Process "$PackageName.$InstallerType" $UnattendedArgs -Wait -Passthru).ExitCode
Write-Verbose "Customization" -Verbose
Write-Verbose "Stop logging" -Verbose
$EndDTM = (Get-Date)
Write-Verbose "Elapsed Time: $(($EndDTM-$StartDTM).TotalSeconds) Seconds" -Verbose
Write-Verbose "Elapsed Time: $(($EndDTM-$StartDTM).TotalMinutes) Minutes" -Verbose
Stop-Transcript