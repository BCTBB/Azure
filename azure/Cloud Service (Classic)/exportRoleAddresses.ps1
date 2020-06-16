# Usage ./powershellscript.ps1 -Slot "Staging" -Service "service_name" -env "environment_tag"
# Need to make sure the Subscription is set or else script will not run
# param([string] $Service = "arbitrary_service_name",
#       [string] $Slot = "Staging",
#       [string] $Path = "c:\path\to\store\export\file",
#       [string] $env = "arbitrary_tag_name",
#       [string] $roleName = "arbitrary.Web")

param([string] $Service = "arbitrary_service_name",
      [string] $Slot = "Staging",
      [string] $Path = "c:\path\to\store\export\file",
      [string] $env = "arbitrary_tag_name",
      [string] $roleName = "arbitrary.Web")

$instanceRole = Get-AzureRole -ServiceName $Service -Slot $Slot -InstanceDetails -RoleName $roleName
if (Test-Path -Path "$Path\output+$env.json")
{
    Remove-Item -Path "$Path\output+$env.json"
}

$count = 0
$maxCount = 0
foreach($cinstance in $instanceRole)
{
    $maxCount++
}

foreach($instance in $instanceRole) {
   if ($count -eq 0)
   {
       echo "writing 1"
       write-output "{"""$instance.Instancename""": """$instance.IPAddress""","| add-content $Path\output+$env.json -NoNewline
   }
   elseif ($count -gt 0 -and $count -ne $maxCount-1)
   {
       echo "writing 2"
       write-output """"$instance.Instancename""": """$instance.IPAddress""","| add-content $Path\output+$env.json -NoNewline
   }
   elseif ($count -eq $maxCount-1)
   {
       echo "writing 3"
       write-output """"$instance.Instancename""": """$instance.IPAddress""""| add-content $Path\output+$env.json -NoNewline
   }
   $count++
}
write-output "}"| add-content $Path\output+$env.json -NoNewline