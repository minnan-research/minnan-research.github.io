cd /d "%~dp0"
type other_chars.txt kautian.csv docs\mispronunciation\index.html docs\mistranslation\index.md > combined.txt
pyftsubset docs/fonts/TauhuOo20.05-Regular.woff2 --text-file=combined.txt --output-file=docs/fonts/TauhuOo20.05-Regular-subset.woff2 --flavor=woff2

del combined.txt
pause
