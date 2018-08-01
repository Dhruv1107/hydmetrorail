import sqlite3
import cgi

form = cgi.FieldStorage() 

username = form.getvalue('name')
userpass = form.getvalue('pass')
userpass1 = form.getvalue('pass1')
ret=0
row=[];


db=sqlite3.connect('metro1.db');
c = db.cursor()
query="UPDATE passenger SET pass=? WHERE uname=?"
ret = c.execute(query,(userpass,username))
row=c.fetchall()
db.commit()
c.close()
db.close()

if ret:
	print("Content-type:text/html\r\n\r\n")
	print('''
	<html>
	<head>
	<title>Password Changed</title>
	</head>
	<body>
	''')
	print('''
	<tr>
	<th> <a href="first.html">Click here to login again</a></th>
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
	print("Invalid Credentials please check!!.....")
	print('''
	</body>
	</html>
	''')



		
