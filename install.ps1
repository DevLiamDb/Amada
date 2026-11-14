# Installs PinkHouse, the Windows app that runs Amada.
#
#   irm https://raw.githubusercontent.com/DevLiamDb/Amada/main/install.ps1 | iex
#
# Finds the newest PinkHouse release of github.com/DevLiamDb/Amada (tags pinkhouse-v...), downloads
# PinkHouse_Setup_<version>_x64.exe, checks its SHA-256 against the one GitHub publishes for the file,
# then opens the installer. No admin rights needed: PinkHouse installs for the current Windows user.
# Nothing else is downloaded: the app downloads an Amada model later, when you choose one in MODELS.

& {
    $ErrorActionPreference = 'Stop'
    $ProgressPreference = 'SilentlyContinue'   # Invoke-WebRequest is much faster without its progress bar
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

    $repo = 'DevLiamDb/Amada'

    if ($env:OS -ne 'Windows_NT') {
        Write-Host 'PinkHouse runs on Windows only.' -ForegroundColor Red
        return
    }
    if (-not [Environment]::Is64BitOperatingSystem) {
        Write-Host 'PinkHouse needs 64-bit Windows.' -ForegroundColor Red
        return
    }

    Write-Host 'Looking for the latest PinkHouse release...'
    $headers = @{ 'User-Agent' = 'PinkHouse-installer'; 'Accept' = 'application/vnd.github+json' }
    $releases = Invoke-RestMethod -Uri "https://api.github.com/repos/$repo/releases?per_page=100" -Headers $headers
    $release = $releases | Where-Object { $_.tag_name -like 'pinkhouse-v*' -and -not $_.draft -and -not $_.prerelease } |
        Sort-Object { [datetime]$_.published_at } -Descending | Select-Object -First 1
    if (-not $release) {
        Write-Host "No PinkHouse release found on github.com/$repo." -ForegroundColor Red
        return
    }
    $asset = $release.assets | Where-Object { $_.name -like 'PinkHouse_Setup_*_x64.exe' } | Select-Object -First 1
    if (-not $asset) {
        Write-Host "$($release.name) has no PinkHouse_Setup_..._x64.exe file." -ForegroundColor Red
        return
    }

    # The SHA-256 GitHub computed for the uploaded file; else the SHA256SUMS.txt published with the release.
    $expected = $null
    if ($asset.digest -like 'sha256:*') {
        $expected = $asset.digest.Substring(7)
    } else {
        $sums = $release.assets | Where-Object { $_.name -eq 'SHA256SUMS.txt' } | Select-Object -First 1
        if ($sums) {
            $text = (Invoke-WebRequest -Uri $sums.browser_download_url -Headers $headers -UseBasicParsing).Content
            if ($text -is [byte[]]) { $text = [Text.Encoding]::UTF8.GetString($text) }
            $line = ($text -split "`n") | Where-Object { $_ -match [regex]::Escape($asset.name) } | Select-Object -First 1
            if ($line) { $expected = ($line.Trim() -split '\s+')[0] }
        }
    }
    if (-not $expected) {
        Write-Host 'No SHA-256 published for the installer: stopping, nothing was installed.' -ForegroundColor Red
        return
    }

    $folder = Join-Path $env:TEMP ('PinkHouse-install-' + [guid]::NewGuid().ToString('N').Substring(0, 8))
    New-Item -ItemType Directory -Path $folder | Out-Null
    $file = Join-Path $folder $asset.name
    try {
        $mb = [math]::Round($asset.size / 1MB)
        Write-Host "Downloading $($asset.name) ($mb MB)..."
        Invoke-WebRequest -Uri $asset.browser_download_url -Headers $headers -OutFile $file -UseBasicParsing

        $actual = (Get-FileHash -Path $file -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($actual -ne $expected.ToLowerInvariant()) {
            Write-Host 'The download is damaged (its SHA-256 does not match the release). Nothing was installed. Try again.' -ForegroundColor Red
            return
        }
        Write-Host "SHA-256 checked: $actual" -ForegroundColor Green

        Write-Host "Opening the installer of $($release.name)..."
        # WaitForExit, not -Wait: -Wait would also wait for PinkHouse itself when the installer starts it at the end.
        $setup = Start-Process -FilePath $file -PassThru
        $setup.WaitForExit()
        if ($setup.ExitCode -eq 0) {
            Write-Host 'Done. Open PinkHouse from the Start menu, then pick a model in MODELS (Amada 4.0 INT4 is the light one, 188 MB).' -ForegroundColor Green
        } else {
            Write-Host "The installer closed without installing (code $($setup.ExitCode))." -ForegroundColor Yellow
        }
    } finally {
        Remove-Item -Path $folder -Recurse -Force -ErrorAction SilentlyContinue
    }
}
