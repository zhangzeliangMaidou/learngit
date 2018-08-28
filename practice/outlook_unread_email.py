#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import os
import traceback
import win32com.client
from log import Logger

Logger = Logger(__file__.split("/")[-1].split(".")[0])
logger = Logger.logger()

class ReadOutlook():

    def __init__(self):
        self.logger = logger
        self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        self.inbox = self.outlook.GetDefaultFolder(win32com.client.constants.olFolderInbox)
        self.unread_mail_id = []
        self.body = ""
        if os.path.isfile("qualcomm_release_info.txt"):
            os.remove("qualcomm_release_info.txt")
        self.f = open("qualcomm_release_info.txt", "a")

    def get_unread_mail(self):
        self.mail_count = self.inbox.Items.Count
        self.logger.debug("self.mail_count:%s"%self.mail_count)
        for i in range(1,self.mail_count):
            if self.inbox.Items[i].UnRead:
                self.unread_mail_id.append(i)

    def read_unread_mail(self):
        for i in self.unread_mail_id:
            message = self.inbox.Items[i]
            try:
                if hasattr(message, "SenderName"):
                    if "nds@noemail.qualcomm.com" == message.SenderName:
                    # if "张泽亮" == message.SenderName:
                        self.logger.debug("Receive nds@noemail.qualcomm.com mail")
                        if hasattr(message, "Subject"):
                            pattern = re.compile(r"Qualcomm(.*)ChipCode(.*)\|(.*)xiaomi-inc(.*)\/(.*)sm8150-la-1-0_amss_standard_oem(.*)\|(.*)Update(.*)Release(.*)Notification")
                            # pattern = re.compile(r"Qualcomm ChipCode | xiaomi-inc / sm8150-la-1-0_amss_standard_oem | Update Release Notification")
                            m = pattern.match(message.Subject)
                            if m:
                                self.logger.debug(message.Subject)
                                if hasattr(message, "Body"):
                                    self.body = message.Body
                                    message.GetConversation().MarkAsRead()
                                    self.logger.debug(i)
                                    return True
                                else:
                                    message.GetConversation().MarkAsRead()
                                    i += 1
                            else:
                                message.GetConversation().MarkAsRead()
                                i += 1
                    else:
                        i += 1
                        message.GetConversation().MarkAsRead()
            except Exception as e:
                self.logger.debug("Read Email Error: %s"%str(e))
                i+=1
        return False

    def get_release_version(self):
        lines = self.body.split("\n")
        for body in lines:
            match_realse_version = re.match(r'(.*)Release:.*', body, re.M | re.I)
            if match_realse_version:
                self.logger.debug(match_realse_version.group())
                realse_version = match_realse_version.group()
                self.f.write("\nrealse version:"+realse_version)
                self.f.flush()

    def get_buildor_label(self):
        lines = self.body.split("\n")
        for line in lines:
            match_buildor_label = re.match(r'(.*)LA\.UM\.(.*)-(.*)-(.*)-(.*)', line, re.M | re.I)
            if match_buildor_label:
                self.logger.debug("buildor_label_info:",match_buildor_label.group())
                buildor_label_info = match_buildor_label.group()
                self.f.write("\nbuildor label number:" + buildor_label_info)
                self.f.flush()
                self.f.close()

def main():

    try:
        readOutlook = ReadOutlook()
        readOutlook.get_unread_mail()
        # while True:
        #     if readOutlook.read_unread_mail():
        #         return True
        #     else:
        #         time.sleep(300)
        #         continue
        readOutlook.read_unread_mail()
        readOutlook.get_release_version()
        readOutlook.get_buildor_label()
    except Exception as e:
        traceback.print_exc()
        logger.warning("exec failed, failed msg:" + traceback.format_exc())

if __name__ == "__main__":
    main()

