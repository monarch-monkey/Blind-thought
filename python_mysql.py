
#链接数据表TESTDB

import pymysql

db = pymysql.connect("localhost","root","441669598","TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()





			   






