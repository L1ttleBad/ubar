#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
not_set = 0
try:
    from private_email_config import mail_host, mail_user, mail_pass, sender, receivers, send_from_name, send_to_name
except:
    print('mail config may not have been set')
    not_set = 1
    

def send(info, subject='Train over.'):
    # 第三方 SMTP 服务
    if not_set:
        print('mail config not set, will not send anything')
        return 1
        
    
    message = MIMEText('Please check!\n'+info, 'plain', 'utf-8')
    message['From'] = send_from_name
    message['To'] =  send_to_name
    
    message['Subject'] = Header(subject, 'utf-8')
    
    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        # print('connect fin.')
        smtpObj.login(mail_user,mail_pass)  
        # print('log fin.')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
        
# send('loss:xxx time: 3h partial result:   xxxxxx')

def save_hist(hist,hist_path):
    with open(hist_path,'w') as file:
        for i in range(len(hist['loss'])):
            string = 'ep: '+str(i)+' loss: '+str(hist['loss'][i])+' val_loss: '+str(hist['val_loss'][i])+'\n'
            file.write(string)
            
def save_hist_acc(hist,hist_path):
    with open(hist_path,'w') as file:
        for i in range(len(hist['loss'])):
            string = 'ep: '+str(i)+' loss: '+str(hist['loss'][i])+' acc: '+str(hist['acc'][i])+'\n'
            file.write(string)
            
if __name__ == '__main__':
    send('test message')