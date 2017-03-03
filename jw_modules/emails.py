#coding: utf-8
'''
Created on 2016-1-26
updated on 2016-3-16
@author: xuhao
Description:发送html格式邮件及添加图片附件
'''
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time

import newfile
import fileFilter

def send_mail():  
    sender = 'hxu@jointwisdom.cn'
    ##    receiver = ['bcao@jointwisdom.cn','hxu@jointwisdom.cn','cma@jointwisdom.cn','mwang@jointwisdom.cn','xzhang@jointwisdom.cn']
    receiver = ['hxu@jointwisdom.cn','2496809691@qq.com']  
    subject = u'测试小组自动化测试报告邮件'  
    smtpserver = 'smtp.exmail.qq.com'  
    username = 'hxu@jointwisdom.cn'  
    password = 'Xuhao0316' 
      
    # Create message container - the correct MIME type is multipart/alternative.  
    msg = MIMEMultipart('alternative')  
    msg['Subject'] = u"测试小组自动化测试报告"  

    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')

    # Create the body of the message (a plain-text and an HTML version).  
    #text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    filename = newfile.new_file()
    #print filename
    for fn in filename:
        if fn.endswith(('.html')):
            result_dir = '..\\report'
            filepath = os.path.join(result_dir,fn)
            url = "file:///"+filepath
            #print url
            text = "Hi!\nHow are you?\nHere is the link you wanted:\n" + url
            f = open(filepath, 'rb')
            mail_body = f.read()
            f.close()
      
            # Record the MIME types of both parts - text/plain and text/html.  
            part1 = MIMEText(text, 'plain')  
            #part2 = MIMEText(html, 'html')
            part2 = MIMEText(mail_body,_subtype='html',_charset='utf-8')
      
            # Attach parts into message container.  
            # According to RFC 2046, the last part of a multipart message, in this case  
            # the HTML message, is best and preferred.  
            msg.attach(part1)  
            msg.attach(part2)
            
    #构造附件
        #获取report下所有的图片
    filename = fileFilter.imgFile()
    for fn in filename:
        if fn.endswith(('.gif','.jpg','.png')):
##            print "****"
##            print fn
            result_dir = '..\\report'
            filepath = os.path.join(result_dir,fn)
        
            att = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')  
            att["Content-Type"] = 'application/octet-stream'
##            att["Content-Disposition"] = 'attachment; filename="screenshot_error.png"'
            att["Content-Disposition"] = 'attachment; filename="%s"'%fn
            msg.attach(att)  

    try: 
        smtp = smtplib.SMTP()  
        smtp.connect('smtp.exmail.qq.com')  
        smtp.login(username, password)  
        smtp.sendmail(sender, receiver, msg.as_string())  
        smtp.quit()
        return True
    except Exception, e:  
        #print str(e)  
        return False 


if __name__ == '__main__':  
    send_mail()

