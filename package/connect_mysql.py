# -*- coding:utf-8 -*- 
"""
@project: PythonStudy
@filename：connect_mysql
@Author: duzhengjun
@create_time：2019-05-19 15:20
@detail：Don't stop learning!!!
@Motto：Sow nothing, reap nothing
"""
import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='940927',db='leva',port=3306,charset='utf8')
# 链接数据库
print("打印数据库链接对象{}".format(conn))
# 获取游标
cur = conn.cursor()
'''
# 创建表
cur.execute("drop table if EXISTS  pyTest")
sql="""create table pyTest (
      id VARCHAR(20) NOT NULL  PRIMARY KEY,
      name VARCHAR(20),
      sex CHAR(2)
    )"""
cur.execute(sql)

#cur.execute(sql) 这个只是执行了你 sql 中的语句，如果对表进行了修改 只执行这一句并没有作用，
#需要在后面加上conn.commit()提交增删改数据到数据库

#添加数据
sql="insert into pyTest(id,name,sex)values('123','张三','男')"
try:
    #执行sql语句
    cur.execute(sql)
    # #提交到数据库执行
    conn.commit()
except:
    #发生错误时回滚
    conn.rollback()

# ----------修改数据-----------------------
#写法1：sql="update pyTest set name='李四' where id='%s'" %('123')
#写法2：
sql = "update pyTest set name='王五' where id='123'"
try:
    cur.execute(sql)
    conn.commit()
except:
    conn.rollback()
'''
#查询操作
def mysql_select():
    sql = input("请输入SQL语句：")
    cur.execute(sql)
    conn.commit()
    #使用 fetchall() 方法获取数据对象，可以得到表中所有的信息，如：(('123', '王五', '男'), ('124', '张三', '男'))
    data1 = cur.fetchall()
    # print("数据对象是{}".format(data1))
    for i in data1:
        print(i)
    cur.close()
    conn.close()
mysql_select()
#使用 fetchone() 方法获取一条数据，如：('123', '王五', '男')
# data2 = cur.fetchone()
# #cur.fetchall()与cur.fetchone() 不能同时使用哪怕赋值给不同的变量。
# print(data2)
# for i in data2:
#     print(i)

# 删除表
# sql = " DROP TABLE pytest"

# cur.close()
# conn.close()


# ----------删除数据-----------------------
# sql="delete from pyTest"
# try:
#     cur.execute(sql)
#     conn.commit()
# except:
#     conn.rollback()