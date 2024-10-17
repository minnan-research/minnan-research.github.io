cd /d "%~dp0"
type other_chars.txt kautian.csv docs\mispronunciation\index.html docs\mistranslation\index.md > combined.txt
pyftsubset docs/fonts/Iansui-Regular.ttf --text-file=combined.txt --output-file=docs/fonts/Iansui-Regular-subset.ttf
del combined.txt
pause
