import sqlite3
import cgi

form = cgi.FieldStorage() 

username = form.getvalue('username')
pass1 = form.getvalue('userpass1')
pass2 = form.getvalue('userpass2')
sques = form.getvalue('sques')
sans= form.getvalue('ans')
balance = 0

ret=0

db=sqlite3.connect('metro1.db');
c = db.cursor()

ret=c.execute("INSERT INTO passenger VALUES(?,?,?,?,?)",(username,pass1,sques,sans,balance))
db.commit()
db.close()

print("Content-type:text/html\r\n\r\n")
print('''
<html>
<head>
<title>Inserted</title>
</head>
<body>
''')
print('''<table border="1" align="center">
<tr>
<th>{0} record inserted successfully...</th>
</tr>
'''.format(ret))
print('''
<tr>
<th> <a href="register.html"> Back</a></th>
</tr>
</table>

</body>
</html>
''')


