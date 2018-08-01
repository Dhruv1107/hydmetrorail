import sqlite3
import cgi

form = cgi.FieldStorage() 

cardno = form.getvalue('cardno')
amt = form.getvalue('amt')

db=sqlite3.connect('metro1.db');
c = db.cursor()

query="UPDATE recharge SET balance=balance+? WHERE cardnum=?"
ret = c.execute(query,(amt,cardno))
db.commit()
c.close()
db.close()

if ret:
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
	<th> <h1>Recharged Successfully</h1><a href="homepage.html">Click here to go to homepage</a></th>
	</tr>
	</table>
	</body>
	</html>
	''')
else:
	print("Content-type:text/html\r\n\r\n")
	print('''
	<html>
	<head>
	<title>login</title>
	</head>
	<body>
	''')
	print("Recharge unsuccesful")
	print('''
	</body>
	</html>
	''')