"""
This takes a large text file for input and turns it into an HTML table 
with two lines per row and one empty column to the right.
To use it: 
Use tableall.sh when that script and this script are both in a
folder full of .txt files.
To get it to show up as a table in Google Docs:
One way to do it is to open the resulting html file in a browser,
then select all, paste into Google Docs, and edit table properties.
A better way would be to edit the script to print a table with a border.
"""
import sys

filename=sys.argv[1]

print filename

f=open(filename)
lines=f.readlines()
line_count = sum(1 for line in open(filename))
index = 0
start = 0
end = 2


print '<table style="width:100%">'

while index <=line_count:
	print '<tr><td>'
	print '<br>'.join(lines[start:end])
	start = end
	end += 2
	index = start
	print '</td><td></td></tr>'

print '</table>'
