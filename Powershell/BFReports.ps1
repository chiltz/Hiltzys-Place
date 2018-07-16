# Parameter help description
param(
        [String]$BFServer = "192.168.9.200";
        [String]$uribase = "https://${BFserver}:52311/api/";
        [String]$uri = $uribase + "login"
    )
Function Get-BFActionsViaRest
{
    Parm(
            $BFUserID;
            $BFPassword;
            $BFServer;
            $uribase;
            $uri
        )
    Write-Warning "----->>>>> Starting Get-BFActionsViaRest.ps1" 
    $result = Invoke-WebRequest -Uri $uri -Method GET -Headers $headers
    Write-Warning "----->>>>> Rest call to $($url) was $($result.StatusDescription)"
    # Having 'logged in', go request all the actions for the current operator.
    if($result.StatusCode -eq 200) 
    {
        $url = $urlbase + "actions"
        # The next line uses the Invoke-WebRequest cmdlet from v2.0;  The result 
        # comes back as a string.
        $r2 = Invoke-WebRequest -Uri $url -Method GET -Headers $headers
        # The next line uses the Invoke-RestMethod cmdlet from v3.0;  
        # If you use this call, the result comes back as a parsed XMl-structure.
        # $r2 = Invoke-RestMethod -Uri $url -Method GET -Headers $headers
        if ($r2.StatusCode -eq 200)
        {
            Write-Warning "Returned result was: $($r2.Content)"
        }
        else
        {
            Write-Warning "Error on action-request: $($r2.status)"
        }
    }
}
$Creds = Get-credential
$BFUserID = $Creds.username
$BFPassword = $Creds.password
Get-BFActionsViaRest -BFUserid $BFUserID -BFPassword $BFPassword -BFServer $BFServer -uribase $urlbase -url $uri

asdfasdfasfd