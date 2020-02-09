"""
Group 2
2/3/2020
Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, Nicholas Fay
"""
#!/bin/sh
here="`dirname \"$0\"`"
echo "cd-ing to $here"
cd "$here" || exit 1

rm -r /Applications/ccs_main.app

cp -r dist/ccs_main.app /Applications

mkdir ~/Library/Application\ Support/CCS/

cp -n Sampleinput.tsv ~/Library/Application\ Support/CCS/Students.tsv