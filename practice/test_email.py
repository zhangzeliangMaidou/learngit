#! /usr/bin/env pyhon
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

mail_user = "zhang_ze_liang@163.com"
mail_pwd = "zhangzeliang1314"
mail_host = "smtp.163.com"
receivers = ["zhang_ze_liang@163.com","zhang_ze_liang@163.com","zhang_ze_liang@163.com"] 
sender = mail_user

# 创建一个带附件的实例
message = MIMEMultipart()
message["From"] = Header("zhang_ze_liang@163.com")
message["To"] = Header("770679241@qq.com;zhang_ze_liang@163.com")
subject = "Python SMTP 邮件测试"
message["Subject"] = Header(subject,"utf-8")

# 邮件正文内容
message.attach(MIMEText("这是菜鸟教程Pyhon邮件测试","plain","utf-8"))

# 构造附件1，传送当前目录下的test.txt文件
att1 = MIMEText(open("test.txt","r").read())
att1["Content-Type"] = "application/octet-stream"
# 这是filename可以任意写，写什么名字，邮件中就显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的aachment文件
att2 = MIMEText(open("attachemnt.txt","r").read())
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host)  
    smtpObj.login(mail_user,mail_pwd)
    print("OK")
    smtpObj.sendmail(sender,"770679241@qq.com;zhang_ze_liang@163.com", message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
