$results=Get-AzConsumptionUsageDetail -StartDate 01/01/2019 -EndDate 01/01/2020 -IncludeAdditionalProperties
#$subscriptions="subscription-name-foo"
$subscriptions=<subscription name>
foreach ($sub in $subscriptions){
$results | `
    Select InstanceName, UsageQuantity, PreTaxCost | `
    Measure-Object -Sum PreTaxCost | Select-Object @{Label="Pre-Tax Cost"; Expression={“{0:C}” -f ($_.Sum)}} | ConvertTo-Json
}