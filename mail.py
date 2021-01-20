# coding=utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender = '3104182180@qq.com'  # 发件人邮箱账号
my_pass = 'toqqwfcxsumgdgbf'  # 发件人QQ邮箱的SMTP中生成的授权码
my_user = '3485586102@qq.com'  # 收件人邮箱账号

try:
    msg = MIMEText("自动打卡注册成功通知\n通知发送时间：" +str(time.asctime(time.localtime(time.time()))), 'plain', 'utf-8')  # 填写邮件内容
    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['From'] = formataddr(["xsk666", my_sender])
    msg['To'] = formataddr(["username", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "注册成功通知"  # 邮件的主题，也可以说是标题
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.sendmail(my_sender, [my_user, ], msg.as_string())
    server.quit()  # 关闭连接
    print("邮件发送成功")
except Exception:
    print("邮件发送失败")
