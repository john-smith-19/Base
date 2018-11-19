#coding: utf-8    
  
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(sender, password, receivers, mail_subject, mail_content, attach_file_path = ''):

    # 创建一个带附件的实例
    message = MIMEMultipart()

    # 发件人
    message['From'] = _format_addr('发送方 <%s>' % sender)

    # 收件人
    message['To'] =  _format_addr('接收方 <aa@bb.cc>')

    # 邮件标题
    message['Subject'] = Header(mail_subject, 'utf-8').encode()

    #邮件正文内容
    mail_content = '''
    <html>
    <body>
    <h1>Hello</h1>
    <p>send by <a href="http://www.python.org">Python教程</a>...</p>
    </body></html>
    '''
    message.attach(MIMEText(mail_content, 'html', 'utf-8'))

    if len(attach_file_path) > 0:
        # 构造附件1
        att1 = MIMEText(open(attach_file_path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="daily_report_20181102.pdf"'
        message.attach(att1)

    # print(att1)

    # # 构造附件2，传送当前目录下的 w3cschool.txt 文件
    # att2 = MIMEText(open('123.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="w3cschool.txt"'
    # message.attach(att2)

    try:
        #发送邮件
        smtpObj = smtplib.SMTP()
        # smtpObj.set_debuglevel(1) #用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
        
        smtpObj.connect('smtp.qq.com')
        pos1 = sender.find('@')
        user_name = sender[:pos1]

        smtpObj.login(user_name, password)    
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
 

if __name__ == '__main__':
    send_mail(
        sender = '发送邮箱', 
        password = '发送密码',
        receivers = ['接收邮箱1', '接收邮箱2', '接收邮箱3'],
        mail_subject = '温馨提示',
        mail_content = '请查收附件，谢谢！',
        attach_file_path = '123.txt'
        )
