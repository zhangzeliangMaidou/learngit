#encoding=utf-8

import win32com.client, sqlite3
from datetime import datetime

def collectMail():
    #conn = sqlite3.connect(r'D:\Software\SQLiteSpy_1.9.9\outlook.db')
    i = 0
    try:
        #启动outlook进程
        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        folder = outlook.Folders[1]
        print(folder.Name)
        #获取收件箱实例
        inbox = outlook.GetDefaultFolder(6)

        #逐条处理邮件信息
        messages = inbox.Items
        #print(help(messages))
        print (help(messages.Find))
        print ('total messages: %s'%len(messages))
        message = messages.GetLast()
        #print (dir(message))
        #print(help(message))
        i=0
        while message:
            try:
                #邮件标题
                if hasattr(message,"Subject"):
                    subject = message.Subject
                    print("subject:%s"%subject)
                else:
                    print("no subject")

                # try:
                #     #邮件接收时间
                #     if hasattr(message,"ReceivedTime"):
                #         received_time = str(message.ReceivedTime)
                #         print("received_time:%s" % received_time)
                #         received_time = datetime.strptime(received_time, "%m/%d/%y %H:%M:%S")
                #         print("received_time:%s" % received_time)
                # except:
                #     print("no received_time")

                if hasattr(message,"HTMLBody"):
                    html_body = message.HTMLBody
                    #print("html_body:%s" % html_body)
                else:
                    print("no HTMLBody")

                size = int(message.Size)

                #邮件发送人
                if hasattr(message,"SenderName"):
                    sender = message.SenderName
                    print("sender:%s" % sender)
                else:
                    print("no sender")

                #邮件接收人
                if hasattr(message,"To"):
                    receiver = message.To
                    print("receiver:%s" % receiver)
                else:
                    print("no receiver")

                #邮件抄送人
                if hasattr(message,"Cc"):
                    cc = message.Cc
                    print("cc:%s" % cc)
                else:
                    print("no cc")

                #邮件正文
                if hasattr(message,"Body"):
                    body = message.Body
                    #print("body:%s" % body)
                else:
                    print("no body")

                #获取下条邮件内容
                message = messages.GetNext()
                i+=1
                print (message)
            except Exception as e:
                print ("error1:%s"%str(e))
                break
    except Exception as e:
        print ("error2:%s"%str(e))
    finally:
        print ('connection closed')
        #conn.close()

collectMail()


