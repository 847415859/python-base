import pymysql

# 配置连接
db = pymysql.connect(host='192.168.126.100',port=3308,user='root',password='root',database='booksite')

# 连接数据库，获取连接对象
cursor = db.cursor()

# 1. 获取所有数据
sql_str = "select * from bookinfo"
cursor.execute(sql_str)
# 获取所有数据
res_data = cursor.fetchall()
# print(type(res_data))
# for item in res_data:
#     print(item)

# 2。获取一条数据
cursor.execute("select * from bookinfo where id = 1")
res_data = cursor.fetchone()
print(type(res_data))
print(res_data)

# 3.更新数
cursor.execute("update bookinfo set bread = '1111' where id = 1 ")
# 修改必须提交
db.commit()
