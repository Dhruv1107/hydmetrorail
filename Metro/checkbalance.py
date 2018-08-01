import sqlite3
import cgi

form = cgi.FieldStorage() 

cardno = form.getvalue('cardno')

db=sqlite3.connect('metro1.db');
c = db.cursor()

query="SELECT balance FROM recharge WHERE cardnum=?"
c.execute(query,(cardno,))
balance=c.fetchone()
c.close()
db.close()
print("Content-type:text/html\r\n\r\n")
print('''
<html>
<head>
<title>Recharged Successfully</title>
</head>
<body>
''')
print('''
<tr>
<th> <h1>The balance is:
''')
print(balance[0])
print('''</h1><a href="homepage.html">Click here to go to homepage</a></th>
</tr>
</table>
</body>
</html>''')