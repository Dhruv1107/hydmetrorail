import sqlite3
import cgi

form = cgi.FieldStorage() 

cardno = form.getvalue('cardno')
total=0

db=sqlite3.connect('metro1.db');
c = db.cursor()

query="SELECT fromstation,tostation,amount FROM details WHERE cardnum=?"
c.execute(query,(cardno,))
row=c.fetchone()
print("Content-type:text/html\r\n\r\n")
print('''
<html>
<head>
<title>Transactions</title>
</head>
<body>
<table border=1 style="width:50%">
<tr>
<th>From</th>
<th>To</th>
<th>Amount</th>
</tr>
''')
while row is not None:
	#print("Content-type:text/html\r\n\r\n")
	print('''<tr><td>''')
	print(row[0])
	print('''</td><td>''')
	print(row[1])
	print('''</td><td>''')
	print(row[2])
	print('''</td>''')
	total+=row[2]
	row=c.fetchone()
print('''</table><h4>The total amount spent is:''')
print(total)
print('''</h4></body></html>''');
c.close()
db.close()
