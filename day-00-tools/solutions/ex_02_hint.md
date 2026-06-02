# Hints for ex_02

PowerShell:
```
New-Item -ItemType Directory -Path pyweek/labs/day-00 -Force
Set-Content -Path pyweek/labs/day-00/done.txt -Value "I did it"
Get-Content pyweek/labs/day-00/done.txt
Remove-Item -Recurse -Force pyweek
```

macOS / Linux:
```bash
mkdir -p pyweek/labs/day-00
echo "I did it" > pyweek/labs/day-00/done.txt
cat pyweek/labs/day-00/done.txt
rm -rf pyweek
```
