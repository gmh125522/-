#1.组装邮件正文
#2.组装邮件头
#3.连接smtp服务器并发送
import smtplib #连接smtp服务器
from email.mime.text import MIMEText #纯文本
from email.mime.multipart import MIMEMultipart #混合格式
from conf import config
#1.组装邮件正文
msg = MIMEMultipart()
email_body = MIMEText('python发送的邮件','plain','utf-8')#plain 纯文字 html
msg.attach(email_body) #将正文添加msg对象中
#2.组装邮件头
msg['From'] = 'test_results@sina.com'
msg['To'] = '1169952123@qq.com'
msg['Subject'] = "from python"

#4.附件
with open(config.report_file,"rb") as f:
    att_file = f.read()
att = MIMEText(att_file,'base64','utf-8')
att["Content_Type"] = 'application/octet-stream'#声明附件的内容格式MIME数据流格式
att["Content_Disposition"] = "attachment;filename='report.html'" #附件描述信息 filename 是附件显示文件名
msg.attach(att)#将附件添加到消息对象中
#3.连接smtp服务器并发送
smtp = smtplib.SMTP_SSL("smtp.163.com")#建立连接
smtp.login("ivan-me@163.com","hanzhichao123")#登录邮箱
smtp.sendmail("ivan-me@163.com","1169952123@qq.com",msg.as_string())#发送