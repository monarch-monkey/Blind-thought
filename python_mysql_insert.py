#数据库插入操作

import pymysql

db = pymysql.connect("localhost","root","441669598","TESTDB")

cursor = db.cursor()

'''sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
'''
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
        ('Mac', 'Mohan', 20, 'M', 2000)

try:
	
	cursor.execute(sql)
	
	db.commit()
	
except:
		
	db.rollback()
	
db.close()	
