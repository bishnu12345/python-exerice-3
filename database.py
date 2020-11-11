import pymysql

db = pymysql.connect('localhost','root','','training')

print ("connection success")

cursor = db.cursor()
sql = "insert into trainee(name,address) values ('Kamal','Jorpati')"
cursor.execute(sql)
db.commit()
