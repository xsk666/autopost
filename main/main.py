# coding=utf-8
import requests
import json
import getinfo
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

def run(user, UA, cook):
    url1 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code=chzu&stu_code=2020211760&authorityid=0&type=3&pagenum=1&pagesize=1000&stu_range=999&searchkey='
    head = {
        'Host': 'yq.weishao.com.cn',
        'User-Agent': UA,
        'Accept': '*/*',
        'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    # 提交今日打卡
    url3 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
    # 读取个人提交信息
    info = getinfo.data(UA, cook)
    head1 = {
        'Host': 'yq.weishao.com.cn',
        'Connection': 'keep-alive',
        'User-Agent': UA,
        'Accept': '*/*',
        'Content-Length': str(len(str(info))),  # json转文字读取长度，再转为字符串
        'Content-Type': 'application/json',
        'Origin': 'https://yq.weishao.com.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    data = json.loads(requests.post(url3, json=info, headers=head).text)
    if(data.get("data") == "提交成功"):
        print("打卡成功！")
        if (user.get("notice") == "true"):
            print("正在发送邮件···")
            try:
                mail=user.get("email")
                username=user.get("name")
                sender = '3104182180@qq.com'  # 发件人邮箱账号
                msg = MIMEText("To："+username+"\n\t自动健康打卡成功通知\n\t通知发送时间：" + time.strftime("%Y/%m/%d %H:%M")+"\n\n\t\tFrom：运行在github的开源项目", 'plain', 'utf-8')  # 填写邮件内容
            # 括号里的对应发件人邮箱昵称、发件人邮箱账号
                msg['From'] = formataddr(["xsk666", sender])
                msg['To'] = formataddr([username, mail])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
                msg['Subject'] = "健康打卡成功通知"  # 邮件的主题，也可以说是标题
                server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
                # 括号中对应的是发件人邮箱账号、邮箱的SMTP中生成的授权码
                server.login(sender, 'toqqwfcxsumgdgbf')
                # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
                server.sendmail(sender, [mail, ], msg.as_string())
                server.quit()  # 关闭连接
                print("给 "+username+" 的邮件发送成功")
            except Exception:
                print("给 " + username + " 的邮件发送失败")
                err = requests.get('https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=邮件发送失败&desp=用户邮箱:' +
                                      mail+'\n时间：' + time.strftime("%Y/%m/%d %H:%M")).text
                if(json.loads(err).get("errmsg") == "success"):
                    print("已通知开发者")

    elif(data.get("errcode") == 500):
        print("今日打卡已完成，自动打卡取消\n")
