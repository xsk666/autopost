# coding=utf-8
import random
import time

import requests

url = "http://dxx.ahyouth.org.cn/api/"
userInfo = url + 'userInfo'
homeData = url + "homeData"
newLearn = url + 'newLearn'
oldLearn = url + "oldLearn"
learnList = url + "learnList?id="
historyList = url + "historyList"
cultureList = url + 'cultureList?page=1'
cultureDetail = url + "cultureDetail"
imageTextList = url + "imageTextList?page=1"
imageTextDetail = url + "imageTextDetail"
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
    except Exception:
        res = "阅读失败"
    echo(res)
    text = "| " + title + " | " + res + " |\n"
    sleeptime = random.randint(10, 20)
    echo("随机延迟 " + str(sleeptime) + " 秒\n")
    time.sleep(sleeptime)
    return text


text = '| 标题 | 结果 |\n | :---| :--- |\n'

# 每日随机往期学习 1次
try:
    echo("->开始往期学习")
    res = requests.get(historyList, headers=head).json().get("list").get("history")
    res = res[random.randint(0, len(res) - 1)]
    echo("随机选择：" + res.get("remark") + " " + res.get("title"))
    res = requests.get(learnList + str(res.get("id")), headers=head).json().get("list").get("list")
    res = res[random.randint(0, len(res))]
    text += read(oldLearn, res.get("id"), res.get("title"))
    echo("->往期学习成功\n")
except Exception:
    echo("->往期学习失败")

# 每日cultureList任务 2次
try:
    echo("->开始每日文化产品阅读")
    list = requests.post(cultureList, headers=head).json().get("lists").get("data")
    for i in range(0, 2):
        text += read(cultureDetail, list[i].get("id"), list[i].get("title"))
    echo("->每日文化产品阅读完成\n")
except Exception:
    echo("->获取文化产品列表失败")

# 每日imageTextList任务 5次
try:
    echo("->开始每日文章阅读")
    list = requests.post(imageTextList, headers=head).json().get("lists").get("data")
    for i in range(0, 5):
        text += read(imageTextDetail, list[i].get("id"), list[i].get("title"))
    echo("->每日文章阅读完成\n")
except Exception:
    echo("->获取文章列表失败")
try:
    res = requests.post(homeData, headers=head).json().get("list")
    text += "|全省排名|" + str(res.get("province_rank")) + "|\n|组织排名|" + str(res.get("organization_rank")) + "|\n|累计积分|" + str(res.get("score")) + "|\n"
    err = requests.get("https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=青年大学习每日任务完成啦&desp=" + text).json().get("errmsg")
    if err == "success":
        echo("->通知发送成功")
except Exception:
    echo("->出错啦")
