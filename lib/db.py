import pymysql
from conf import config


# # 1. 建立连接
# conn = pymysql.connect(host='115.28.108.130',
#                        port=3306,
#                        user='test',
#                        password='123456',
#                        db='api_test',
#                        charset='utf8')
# # 2. 从连接建立操作游标
# cur = conn.cursor()
# # 3. 用游标执行查询 / 修改 sql语句
# cur.execute("select * from user where name='张三'") # 查询操作
# # cur.execute("delete from user where passwd='1234567'")
# # conn.commit()
# # 4. 获取查询结果 / 提交修改
# r = cur.fetchone()  # cur.fetchall()  # cur.fetchmany(3)
# # print(r)
# # 5. 关闭游标和连接
# cur.close()
# conn.close()


# name = 'lily2'
# sql = "select * from user where name='%s'" % name
# print(sql)

# 封装一个 获取连接的函数
# 封装一个执行数据库查询的函数,返回所有结果
# 封装一个修改数据库的函数
def get_conn():
    conn = pymysql.connect(host=config.db_host,
                           port=config.db_port,
                           user=config.db_user,
                           password=config.db_password,
                           db=config.db,
                           charset='utf8')
    return conn


def db_query(sql):
    config.logging.info(sql)
    c = get_conn()
    cur = c.cursor()
    cur.execute(sql)
    r = cur.fetchall()
    cur.close()
    c.close()
    return r


def db_change(sql):
    config.logging.info(sql)
    print(sql)
    c = get_conn()
    cur = c.cursor()
    try:
        cur.execute(sql)
        c.commit()
    except Exception as e:
        print(repr(e))
        c.rollback()
    finally:
        cur.close()
        c.close()


# 查询用户是否存在
def check_user(name):
    r = db_query("select * from user where name='%s'" % name)
    if r:
      return True
    return False


# 删除用户
def del_user(name):
    db_change("delete from user where name='{}'".format(name))



if __name__ == '__main__':  #判断是不是从当前模块执行的
    print(check_user("gmh12334"))