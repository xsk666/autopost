# coding=utf-8
import smtplib
import time
import requests
from email.mime.text import MIMEText
from email.utils import formataddr


def mail(mail, username):
    # 发送到的邮箱地址，收件人的名称
    try:
        sender = '3104182180@qq.com'  # 发件人邮箱账号
        msg = MIMEText("自动打卡成功通知\n通知发送时间：" + str(time.asctime(
            time.localtime(time.time()))), 'plain', 'utf-8')  # 填写邮件内容
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["xsk666", sender])
        msg['To'] = formataddr([username, mail])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "打卡成功通知"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        # 括号中对应的是发件人邮箱账号、邮箱的SMTP中生成的授权码
        server.login(sender, 'toqqwfcxsumgdgbf')
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(sender, [mail, ], msg.as_string())
        server.quit()  # 关闭连接
        print("给"+username+"的邮件发送成功")
    except Exception:
        print("给"+username+"的邮件发送失败")
        if(wechat('邮件发送失败', '用户邮箱:'+mail) == "success"):
            print("已通知开发者")


def wechat(text, desp):
    # 标题，具体内容
    return json.loads(requests.get('https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text='+text+'&desp='+desp+'\n时间：' +
                                   str(time.asctime(time.localtime(time.time())))).text).get("errmsg")
