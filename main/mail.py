# coding=utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr

import requests


def qq(text, desp):
    return requests.get("https://qmsg.zendee.cn/send/4d762a772660e5bd2c725d1969633815?msg=" + text + "\n\n" + desp).json()


def send(mail, username):
    # 发送到的邮箱地址，收件人的名称
    try:
        sender = '3104182180@qq.com'  # 发件人邮箱账号
        msg = MIMEText("To：" + username + "\n\t自动健康打卡成功通知\n\t通知发送时间：" + time.strftime(
            "%Y/%m/%d %H:%M") + "\n\n\t\tFrom：运行在github的开源项目", 'plain', 'utf-8')  # 填写邮件内容
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["健康打卡通知", sender])
        msg['To'] = formataddr([username, mail])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "健康打卡成功通知"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        # 括号中对应的是发件人邮箱账号、邮箱的SMTP中生成的授权码
        server.login(sender, 'toqqwfcxsumgdgbf')
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(sender, mail, msg.as_string())
        server.quit()  # 关闭连接
        print("给 " + username + " 的邮件发送成功\n")
    except Exception:
        print("给 " + username + " 的邮件发送失败\n")
        err = qq('邮件发送失败', '用户邮箱:' + mail + '\n\n时间：' + time.strftime("%Y/%m/%d %H:%M")).get("errmsg")
        if err == "success":
            print("已通知开发者\n")
