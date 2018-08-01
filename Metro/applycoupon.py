import sqlite3
import cgi

form = cgi.FieldStorage() 

cardno = form.getvalue('cardno')
ccode=form.getvalue('ccode')
row=[];
ret=0

db=sqlite3.connect('metro1.db');
c = db.cursor()

query="SELECT * FROM coupon WHERE code=?"
ret = c.execute(query,(ccode,))    
row=c.fetchall()


if row:
	query1="UPDATE recharge SET balance=balance+10 WHERE cardnum=?"
	ret = c.execute(query1,(cardno,))
	db.commit()
	print("Content-type:text/html\r\n\r\n")
	print('''
	<html>
	<head>
	<h1>Coupon code added! 10 rs added</h1>
	</head>
	<body>
	''')

else:
	print("Content-type:text/html\r\n\r\n")
	print('''
	<html>
	<head>
	<h1>Coupon code incorrect</h1>
	</head>
	<body>
	''')

	
c.close()
db.close()

