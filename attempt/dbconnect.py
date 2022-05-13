import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd="lmy740812", db="course_homework")
cs = conn.cursor()
tup = cs.execute("select * from student3")
print(cs.fetchall()[0])