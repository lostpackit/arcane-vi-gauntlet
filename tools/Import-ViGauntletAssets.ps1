# Safely stage the six Arcane Vi Gauntlet CAD ZIP parts into this existing Git clone.
# Requires PowerShell 5+ and the SHA256 CSV from the ChatGPT download.
# Does NOT run git add/commit/push and does NOT overwrite different existing files.
param(
  [Parameter(Mandatory=$true)][string]$SourceFolder,
  [string]$ManifestPath = ""
)
$ErrorActionPreference = "Stop"
$repo = (Resolve-Path -LiteralPath (Split-Path $PSScriptRoot -Parent)).Path
if (!(Test-Path -LiteralPath (Join-Path $repo ".git"))) {
  throw "This script must run inside the cloned Git repository (missing .git at $repo)."
}
$source = (Resolve-Path -LiteralPath $SourceFolder).Path
if (!$ManifestPath) { $ManifestPath = Join-Path $source "Arcane_Vi_Gauntlet_Assets_SHA256.csv" }
if (!(Test-Path -LiteralPath $ManifestPath)) {
  throw "SHA256 manifest missing: $ManifestPath. Download it alongside the six ZIP parts."
}
$names = @(
  "Arcane_Vi_Gauntlet_Assets_01_Original_3MF.zip",
  "Arcane_Vi_Gauntlet_Assets_02_Original_Arms.zip",
  "Arcane_Vi_Gauntlet_Assets_03_Original_Lights.zip",
  "Arcane_Vi_Gauntlet_Assets_04_V1.zip",
  "Arcane_Vi_Gauntlet_Assets_05_V2.zip",
  "Arcane_Vi_Gauntlet_Assets_06_V3_V4.zip"
)
foreach ($name in $names) {
  $path = Join-Path $source $name
  if (!(Test-Path -LiteralPath $path)) { throw "Missing ZIP part: $path" }
}
$manifest = @(Import-Csv -LiteralPath $ManifestPath)
if ($manifest.Count -ne 61) { throw "Expected 61 manifest entries; found $($manifest.Count)." }
$temp = Join-Path ([System.IO.Path]::GetTempPath()) ("ViGauntletImport_" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $temp -Force | Out-Null
try {
  foreach ($name in $names) {
    Write-Host "Extracting $name ..."
    Expand-Archive -LiteralPath (Join-Path $source $name) -DestinationPath $temp -Force
  }
  foreach ($row in $manifest) {
    $relative = [string]$row.relative_path
    if (!$relative.StartsWith("originals/") -and !$relative.StartsWith("releases/")) {
      throw "Unexpected manifest path: $relative"
    }
    if ($relative.Contains("..")) { throw "Unsafe manifest path: $relative" }
    $file = Join-Path $temp $relative
    if (!(Test-Path -LiteralPath $file -PathType Leaf)) { throw "Missing staged file: $relative" }
    $size = (Get-Item -LiteralPath $file).Length
    if ($size -ne [long]$row.bytes) { throw "Size mismatch: $relative" }
    $hash = (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($hash -ne ([string]$row.sha256).ToLowerInvariant()) {
      throw "SHA256 mismatch: $relative"
    }
  }
  Write-Host "All 61 files passed SHA256 verification."
  $copyPlan = @()
  $copied = 0
  $skipped = 0
  foreach ($row in $manifest) {
    $relative = [string]$row.relative_path
    $from = Join-Path $temp $relative
    $dest = Join-Path $repo $relative
    if (Test-Path -LiteralPath $dest) {
      $existing = (Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash.ToLowerInvariant()
      if ($existing -ne ([string]$row.sha256).ToLowerInvariant()) {
        throw "Different file already exists: $relative. Aborting to protect your work."
      }
      $skipped++
    } else {
      $copyPlan += [pscustomobject]@{ Source = $from; Destination = $dest }
    }
  }
  foreach ($item in $copyPlan) {
    New-Item -ItemType Directory -Path (Split-Path $item.Destination -Parent) -Force | Out-Null
    Copy-Item -LiteralPath $item.Source -Destination $item.Destination -NoClobber
    $copied++
  }
  Write-Host "Import completed: $copied new files, $skipped already matching."
  Write-Host "Next: git lfs install; git add originals releases; git lfs ls-files; git commit; git pull --rebase origin main; git push."
} finally {
  if (Test-Path -LiteralPath $temp) { Remove-Item -LiteralPath $temp -Recurse -Force }
}
