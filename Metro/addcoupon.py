import sqlite3
import cgi

form = cgi.FieldStorage() 

coupon = form.getvalue('coup')

balance = 0

ret=0

db=sqlite3.connect('metro1.db');
c = db.cursor()

ret=c.execute("INSERT INTO coupon VALUES(?)",(coupon,))
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
<th>{0} coupon inserted successfully...</th>
</tr>
'''.format(ret))
print('''
<tr>
<th> <a href="adminhomepage.html"> Back</a></th>
</tr>
</table>

</body>
</html>
''')


