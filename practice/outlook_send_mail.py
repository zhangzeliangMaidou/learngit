#! /usr/bin/env python
# -*- utf-8 -*-

import os
import sys
import time
import zipfile
import traceback
import win32com.client as win32
from log import Logger

Logger = Logger(__file__.split("/")[-1].split(".")[0])
logger = Logger.logger()

class OutlookMail():

    def __init__(self,recevers=None, cc=None, subject=None, body=None, attachments=None):
        """
        recevers    : 收件人,如果发送多个联系人,请在联系人之间使用分号隔开. 如:zhangzeliang@xiaomi.com;caoxingwei@xiaomi.com
        cc          : 抄送人,如果发送多个抄送人,请在抄送人之间使用分号隔开. 如:zhangzeliang@xiaomi.com;caoxingwei@xiaomi.com
        attachments : 附件, 如果发送多个附件,请在附件之间使用分号隔开. 如:D:\work\test.py;D:\work\log\
        """
        self.logger = logger
        self.recevers = [recevers]
        self.cc = [cc]
        self.subject = subject
        self.body = body
        self.attachments = attachments
        self.mail_head = """\n\nDear all,\n\n"""
        self.signature = """\n\n\n\n\nBest Wishes!\n"""+"-"*30+"""\n这是一封自动发送邮件，请勿回信息！\n如有问题，请保留！\n最终解释权-----没有解释权，不需要!\n"""+"-"*30
        self.outlook = win32.Dispatch("Outlook.Application")
        self.mail = self.outlook.CreateItem(0)
        self.attachments_list = []
        self.attachment_list = []
        self.attachment()

    def attachment(self):
        """判断附件是否为文件夹，如果附件中包含文件夹，则把文件夹压缩为zip文件后，添加到邮箱中"""
        if self.attachments:
            if self.attachments.startswith(";"):
                self.attachments = self.attachments[1:]
            if self.attachments.endswith(";"):
                self.attachments = self.attachments[:-1]
            if ";" in self.attachments:
                self.attachments_list = self.attachments.split(";")
            else:
                self.attachments_list.append(self.attachments)
            all_file_size = 0
            for attachment in self.attachments_list:
                if os.path.isfile(attachment):
                    self.attachment_list.append(attachment)
                    all_file_size += os.path.getsize(attachment)
                    continue
                elif os.path.isdir(attachment):
                    dirname = os.path.basename(attachment)
                    zipfilename = dirname+".zip"
                    zipfilepath = os.path.dirname(attachment)+os.sep+zipfilename
                    z = zipfile.ZipFile(zipfilepath, 'w', zipfile.ZIP_DEFLATED)
                    for dirpath, dirnames, filenames in os.walk(attachment):
                        fpath = dirpath.replace(attachment, '')
                        fpath = fpath and fpath + os.sep or ''
                        for filename in filenames:
                            z.write(os.path.join(dirpath, filename), fpath + filename)
                    self.attachment_list.append(zipfilepath)
                    all_file_size += os.path.getsize(zipfilepath)
                    continue
                else:
                    self.logger.debug("Path Error: %s"%attachment)
                    continue
            if all_file_size/1024/1024 < 20:
                return True
            else:
                self.logger.debug("Attachments size is more than 20M, can not send with Outlook Mail")
                self.attachment_list = []

    def send(self):
        try:
            self.mail.To = self.recevers[0]
            self.mail.CC = self.cc[0]
            # 没有邮件主题将无法成功发送邮件
            if self.subject:
                self.mail.Subject = self.subject
            else:
                self.mail.Subject = "Outlook test"
            if self.body:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.mail.Body = self.mail_head+self.body+"\n\n"+current_time+self.signature
            else:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                self.mail.Body = self.mail_head+"Send email via Outlook"+"\n\n"+current_time+self.signature
            if len(self.attachment_list)>0:
                for attachment in self.attachment_list:
                    self.mail.Attachments.Add(attachment)
            self.mail.Send()
            self.logger.debug("Send successfully")
        except Exception as e:
             self.logger.debug ("Sending email with outlook is Failure! ERROR:%s"%str(e))

def main():
    try:
        recevers = "zhangzeliang@xiaomi.com;zhangzeliang@xiaomi.com"
        cc = "zhangzeliang@xiaomi.com;zhangzeliang@xiaomi.com"
        attachments = "D:\work\信息安全.pdf;D:\work"
        outlookMail = OutlookMail(recevers=recevers, cc=cc, attachments=attachments)
        outlookMail.send()
    except Exception as e:
        traceback.print_exc()
        logger.warning("exec failed, failed msg:" + traceback.format_exc())
        
if __name__ == "__main__":
    main()




