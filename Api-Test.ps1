$user = "admin"
$pass = "admin"
$pair = "$($user):$($pass)"

$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))

$basicAuthValue = "Basic $encodedCreds"

$Headers = @{
    Authorization = $basicAuthValue
}


# $credential = [pscredential]::new('admin', (ConvertTo-SecureString 'admin' -AsPlainText -Force))
$base = "http://127.0.0.1:8000/"
$path = "food/"
$uri = $base + $path
invoke-restmethod -Headers $Headers -Uri $uri -Method Get
