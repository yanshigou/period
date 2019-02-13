# -*- coding: utf-8 -*-
__author__ = 'dzt'
__date__ = '2019/02/12 16:13'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# from email import encoders
# from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from datetime import datetime
import requests


# 格式化邮件地址
def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendMail(body, attachment=None):
    smtp_server = 'smtp.qq.com'
    from_mail = 'yanshigou@foxmail.com'
    mail_pass = '授权码非密码'
    to_mail = ['xx@cmx-iot.com', 'xx@cmx-iot.com']  # 列表多个
    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart()
    # Header对中文进行转码
    msg['From'] = formatAddr('yanshigou<%s>' % from_mail).encode()
    msg['To'] = ','.join(to_mail)
    msg['Subject'] = Header('监听nginx情况{0}'.format(datetime.now()), 'utf-8').encode()
    # plain代表纯文本
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    # 二进制方式模式文件
    # with open(attachment, 'rb') as f:
    #     # MIMEBase表示附件的对象
    #     mime = MIMEBase('text', 'txt', filename=attachment)
    #     # filename是显示附件名字
    #     mime.add_header('Content-Disposition', 'attachment', filename=attachment)
    #     # 获取附件内容
    #     mime.set_payload(f.read())
    #     encoders.encode_base64(mime)
    #     # 作为附件添加到邮件
    #     msg.attach(mime)
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_mail, mail_pass)
    # print('kaishi')
    # print(type(msg))
    server.sendmail(from_mail, to_mail, msg.as_string())  # as_string()把MIMEText对象变成str
    server.quit()


def listen_nginx():
    url = 'http://xxx:8000/usermanager/checkLogin/?username=15922504420'
    res = requests.get(url=url)
    # print(res.status_code)
    # print(type(res.status_code))
    return res


if __name__ == "__main__":
    sendMail('附件是测试数据, 请查收！')
