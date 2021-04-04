# coding=utf-8
import random
import time

import requests

url = "http://dxx.ahyouth.org.cn/api/"
todayTask = url + 'todayTask'  # 每日任务
homeData = url + "homeData"  # 主页面
newLearn = url + 'newLearn'  # 本期学习
oldLearn = url + "oldLearn"  # 往期学习
historyList = url + "historyList"  # 往季学习列表
learnList = url + "learnList?id="  # 第id季学习列表
cultureList = url + 'cultureList?page=1'  # 每日文化产品列表
cultureDetail = url + "cultureDetail"  # 文化产品内容
imageTextList = url + "imageTextList?page=1"  # 每日文章列表
imageTextDetail = url + "imageTextDetail"  # 每日文章内容
head = {
    'Host': 'dxx.ahyouth.org.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/4747 ',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'token': 'riPObGOJKPPS4fFu1hvpvRFk5oDgpVGN',
    'Content-Type': 'application/json',
    'Referer': 'http://dxx.ahyouth.org.cn/',
    'X-Requested-With': 'com.tencent.mm',
    'Cookie': 'PHPSESSID=857160ee6000aa7493839c8cfc2cb554'
}


def echo(text):
    print(time.strftime("%m-%d %H:%M:%S", time.localtime()) + "-> " + text)


def read(url, id, title):
    echo("开始阅读：" + title)
    try:
        res = requests.post(url, json={"id": id}, headers=head).json().get("message")
    except requests.exceptions.ConnectionError:
        res = "阅读失败"
    echo(res)
    sleeptime = random.randint(6, 12)
    echo("随机延迟 " + str(sleeptime) + " 秒\n")
    time.sleep(sleeptime)
    return True


text = ''
# 每日登陆
try:
    requests.post(todayTask, headers=head).json()
    text += "每日登陆成功\n"
    echo("每日登陆成功\n")
except requests.exceptions.ConnectionError:
    text += "每日登陆成功\n"
    echo("登陆失败\n")

# 每日随机往期学习 1次
try:
    echo("->开始往期学习")
    res = requests.get(historyList, headers=head).json().get("list").get("history")
    res = res[random.randint(0, len(res) - 1)]
    echo("随机选择：" + res.get("remark") + " " + res.get("title"))
    res = requests.get(learnList + str(res.get("id")), headers=head).json().get("list").get("list")
    res = res[random.randint(0, len(res))]
    if read(oldLearn, res.get("id"), res.get("title")):
        text += "往期学习成功\n"
    echo("->往期学习成功\n")
except requests.exceptions.ConnectionError:
    text += "往期学习失败\n"
    echo("->往期学习失败")

# 每日cultureList任务 2次
try:
    echo("->开始每日文化产品阅读")
    list = requests.post(cultureList, headers=head).json().get("lists").get("data")
    for i in range(0, 2):
        read(cultureDetail, list[i].get("id"), list[i].get("title"))
    text += "每日文化产品阅读完成\n"
    echo("->每日文化产品阅读完成\n")
except requests.exceptions.ConnectionError:
    text += "每日文化产品阅读失败\n"
    echo("->获取文化产品列表失败")

# 每日imageTextList任务 5次
try:
    echo("->开始每日文章阅读")
    list = requests.post(imageTextList, headers=head).json().get("lists").get("data")
    for i in range(0, 5):
        read(imageTextDetail, list[i].get("id"), list[i].get("title"))
    text += "每日文章阅读完成\n"
    echo("->每日文章阅读完成\n")
except requests.exceptions.ConnectionError:
    text += "每日文章阅读失败\n"
    echo("->获取文章列表失败")

try:
    res = requests.post(homeData, headers=head).json().get("list")
    text += "\n全省排名：" + str(res.get("province_rank")) + "\n组织排名：" + str(res.get("organization_rank")) + "\n累计积分：" + str(res.get("score"))
    true = requests.get("https://qmsg.zendee.cn/send/11a4ed5a314c66df757718ba36fea180?msg=青年大学习每日任务完成啦\n\n" + text).json().get("success")
    if true:
        echo("->通知发送成功")
    else:
        echo("->通知发送失败")
except requests.exceptions.ConnectionError:
    echo("->出错啦")
