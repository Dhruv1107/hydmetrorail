import sqlite3
import cgi
from http import cookies

form = cgi.FieldStorage() 

iname = form.getvalue('username')
upass = form.getvalue('userpass')
sele=form.getvalue('select')

ret=0

db=sqlite3.connect('metro1.db');
c = db.cursor()


row=[];
if sele=='Passenger':
	query="SELECT uname,pass FROM passenger WHERE uname=? and pass=?"
	ret = c.execute(query,(iname,upass))    
	row=c.fetchall()
	c.close()
	db.close()

	c = cookies.SimpleCookie()
	c['username'] = iname
	c['userpass'] = upass
	if row:
			print("Content-type:text/html\r\n\r\n")
			print('''
			<html>
			<head>
			<title>login</title>
			</head>
			<body>
			''')
			print('''
			<tr>
			<th> <a href="homepage.html">Click here to enter</a></th>
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
		   print("Invalid Id.....")
		   print('''
		   </body>
		   </html>
		   ''')
elif sele=='Admin':
	query="SELECT uname,pass FROM admin WHERE uname=? and pass=?"
	ret = c.execute(query,(iname,upass))    
	row=c.fetchall()
	c.close()
	db.close()

	c = cookies.SimpleCookie()
	c['username'] = iname
	c['userpass'] = upass

	if row:
			print("Content-type:text/html\r\n\r\n")
			print('''
			<html>
			<head>
			<title>login</title>
			</head>
			<body>
			''')
			print('''
			<tr>
			<th> <a href="adminhomepage.html">Click here to enter</a></th>
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
		   print("Invalid Id.....")
		   print('''
		   </body>
		   </html>
		   ''')


