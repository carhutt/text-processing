A=10
B=5
len=`wc -l < all.txt`
len2=$((len / 5))

while [ $A -le $len2 ]; do
	chunk=`head -$A all.txt | tail -$B`
	awk -v var="$chunk"'
	BEGIN{print " "} 
    {printf("<tr><td>"$chunk"</td><td></td></tr>\n")}
    END{print " "}
    ' | tee -a table.html
	let A+=5
done