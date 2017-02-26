"""
This takes a large text file for input and turns it into an HTML table 
with five lines per row and one empty column to the right.
To use it: 
Edit the opening definitions to reference the text file you're using.
Run it from the terminal like so:
$ python htmlchunk.py > table.html
"""

f=open('IDC_text.txt')
lines=f.readlines()
line_count = sum(1 for line in open('IDC_text.txt'))
index = 0
start = 0
end = 1


print '<table style="width:100%">'

while index <=line_count:
	print '<tr><td>'
	print '<br>'.join(lines[start:end])
	start = end
	end += 1
	index = start
	print '</td><td></td></tr>'

print '</table>'