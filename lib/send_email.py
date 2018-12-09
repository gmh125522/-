import smtplib #连接smtp服务器
from email.mime.text import MIMEText #纯文本
from email.mime.multipart import MIMEMultipart #混合格式
from conf import config
def send_report():
    #1.组装邮件正文
    msg = MIMEMultipart()
    email_body = MIMEText(config.body,'plain','utf-8')#plain 纯文字 html
    msg.attach(email_body) #将正文添加msg对象中
    #2.组装邮件头
    msg['From'] = config.smtp_user
    msg['To'] = config.smtp_user
    msg['Subject'] = config.subject

    #4.附件
    with open(config.report_file,"rb") as f:
        att_file = f.read()
    att = MIMEText(att_file,'base64','utf-8')
    att["Content_Type"] = 'application/octet-stream'#声明附件的内容格式MIME数据流格式
    att["Content_Disposition"] = "attachment;filename='report.html'" #附件描述信息 filename 是附件显示文件名
    msg.attach(att)#将附件添加到消息对象中
    #3.连接smtp服务器并发送
    smtp = smtplib.SMTP_SSL(config.smtp_server)#建立连接
    smtp.login(config.smtp_user,config.smtp_password)#登录邮箱
    smtp.sendmail(config.smtp_user,config.receiver,msg.as_string())#发送
is_send_report = False
if __name__=="__main__":
    send_report()