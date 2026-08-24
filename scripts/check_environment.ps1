$ErrorActionPreference = 'SilentlyContinue'

$repoRoot = Split-Path -Parent $PSScriptRoot
$requiredFiles = @(
    'README.md',
    'prompts.md',
    'presentation.tex',
    'presentation.pdf',
    'AGENTS.md',
    'analysis\variance_derivation.md',
    'code\variance_extension.py',
    'output\variance_summary.txt',
    'output\variance_results.csv',
    'output\variance_curve.svg',
    'hand\README.md',
    'hand\DERIVATION_GUIDE.md'
)

Write-Host 'Tool readiness'
$tools = @('git', 'gh', 'code', 'node', 'npm', 'codex', 'tectonic')
foreach ($tool in $tools) {
    $command = Get-Command $tool -ErrorAction SilentlyContinue
    if ($command) {
        $version = (& $tool --version 2>$null | Select-Object -First 1)
        Write-Host ('[OK] {0}: {1}' -f $tool, $version)
    } else {
        Write-Host ('[MISSING] {0}' -f $tool)
    }
}

Write-Host "`nRepository readiness"
foreach ($relativePath in $requiredFiles) {
    $fullPath = Join-Path $repoRoot $relativePath
    if (Test-Path -LiteralPath $fullPath) {
        Write-Host ('[OK] {0}' -f $relativePath)
    } else {
        Write-Host ('[MISSING] {0}' -f $relativePath)
    }
}

$handFiles = @(Get-ChildItem -LiteralPath (Join-Path $repoRoot 'hand') -File |
    Where-Object { $_.Name -notin @('README.md', 'DERIVATION_GUIDE.md') })
if ($handFiles.Count -gt 0) {
    Write-Host ('[OK] handwritten evidence: {0} file(s)' -f $handFiles.Count)
} else {
    Write-Host '[TODO] add a genuine handwritten photo to hand/'
}

Push-Location $repoRoot
try {
    Write-Host ('Branch: {0}' -f (git branch --show-current))
    if (Select-String -Path 'README.md', 'presentation.tex' -Pattern 'TODO' -Quiet) {
        Write-Host '[TODO] unresolved TODO markers remain'
    } else {
        Write-Host '[OK] no TODO markers in README or presentation'
    }
} finally {
    Pop-Location
}
