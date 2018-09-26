
#删除数据库内容

import pymysql

db = pymysql.connect("localhost","root","441669598","TESTDB")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)

try:
	
	cursor.execute(sql)
	
	db.commit()

except:
	
	db.rollback()
	
db.close()	