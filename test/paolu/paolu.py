# coding=utf-8
import requests
import json
import os
import re
import time


def surplus(head, email):
    try:
        response = requests.get("https://paoluz.link/user", headers=head).text
        pattern = re.search(r'<span class="counter">(.)+</span>...', response, re.M | re.I).group()
        pattern = pattern[22:25] + pattern[-2:]
        return pattern
    except Exception:
        return "解析失败"


def checkin(head, email):
    response = json.loads(requests.post("https://paoluz.link/user/checkin", headers=head).text)
    msg = response.get("msg")
    if (response.get("ret") == 1):
        print(email + " 签到成功")
        text = "签到账号：【" + email + "】\n\n签到数据：【" + msg + "】\n\n"+"剩余流量【"+surplus(head, email)+"】\n\n签到时间：【" + time.asctime(time.localtime(time.time())) + "】\n\n"
        return text
    else:
        text = "签到账号：【" + email + "】\n\n剩余流量：【"+surplus(head, email)+"】\n\n签到时间：【" + time.asctime(time.localtime(time.time())) + "】\n\n"
        print(email+" 已签到")
        return text


def login(uuid, email, password):
    head = {
        'cookie': "__cfduid="+uuid+";lang=zh-cn",
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        "email": email,
        "passwd": password,
        "code": ""
    }
    response = requests.post("https://paoluz.link/auth/login", data=data, headers=head)
    test = response.headers["set-cookie"].split("=")
    uid = test[1]
    key = test[9]
    ip = test[13]
    expire = test[17]
    head = {"cookie": "__cfduid=" + uuid + ";lang=zh-cn;cnxad_lunbo=yes;_ga=GA1.2.1656003110.1594518881;_gid=GA1.2.1056328585.1594518881;uid=" +
            uid + ";email=" + email + ";key=" + key + ";ip=" + ip + ";expire_in=" + expire}
    return checkin(head, email)


def onSign(email, password):
    cfuid = requests.get("https://paoluz.link/auth/login").headers["set-cookie"].split(";")[0]
    return login(cfuid, email, password)


# 循环读取文件
ff = open(os.getcwd() + "/test/paolu/users.json")
users = json.loads(ff.read())
ff.close()
text = ''
print("开始 "+time.strftime("%Y/%m/%d")+" 签到")
for i in range(0, len(users)):
    print("开始为 "+users[i].get('account')+" 签到")
    text += onSign(users[i].get('account'), users[i].get("passwd"))
print("签到完成")
requests.get('https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=跑路云签到结果通知&desp='+text)
