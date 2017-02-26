# This is the working script.  It takes a large text file for input
# and turns it into an HTML table with five lines per row and one
# empty column to the right.

f=open('all.txt')
lines=f.readlines()
index = 0
start = 0
end = 5

print '<table style="width:100%">'

while index <=605:
	print '<tr><td>'
	print '<br>'.join(lines[start:end])
	start = end
	end += 5
	index = start
	print '</td><td></td></tr>'

print '</table>'