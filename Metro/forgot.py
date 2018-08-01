import sqlite3
import cgi
from http import cookies

form = cgi.FieldStorage() 

username = form.getvalue('username')
sques = form.getvalue('sques')
sans = form.getvalue('ans')
ret=0
row=[];

db=sqlite3.connect('metro1.db');
c = db.cursor()

query="SELECT uname FROM passenger WHERE uname=? and sques=? and sans=?"
ret = c.execute(query,(username,sques,sans))  
row=c.fetchall()
c.close()
db.close()

D = cookies.SimpleCookie()
D["username"] = form.getvalue('username')

if row:
		print("Content-type:text/html\r\n\r\n")
		print('''
		<html>
		<head>
		<title>Reset your Password</title>
		</head>
		<body>
		''')
		print('''
		<tr>
		<th> <a href="reset.html">Click here to reset your password</a></th>
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