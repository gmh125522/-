#数据库配置
db_host='115.28.108.130'
db_port=3306
db_user='test'
db_password='123456'
db='api_test'

#路径配置 绝对路径
import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#__file__ 当前文件 os.path.abspath()绝对路径 os.path.dirname（）所在文件夹路径
#数据文件目录
data_path = os.path.join(project_path,'data')
data_file = os.path.join(project_path,'data','data.xlsx')
#日志文件根目录
log_file = os.path.join(project_path,'log','log.txt')
#报告文件路径
report_file = os.path.join(project_path,'report','report.html')


#log配置
import  logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="w"
                    )
if __name__=="__main__":
   # logging.info("hello,word")
   # logging.info("中文")
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(data_path)
    print(log_file)
    print(report_file)

#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'ivan-me@163.com'
smtp_password = 'hanzhichao123'

receiver = '1169952123@qq.com'
subject = '接口测试报告'
body = 'hi,all,\n附件是接口测试报告，请查收。'
is_send_report = False
#if __name__=="__main__":
