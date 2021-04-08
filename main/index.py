# coding=utf-8
import json
import os
import random
import sys
import time
from shutil import rmtree as remove

import requests

import post
import sign


def qq(text, desp):
    qmsg = "11a4ed5a314c66df757718ba36fea180"
    return requests.get("https://qmsg.zendee.cn/send/" + qmsg + "?msg=" + text + "\n\n" + desp).json()


print("开始 " + time.strftime("%Y/%m/%d") + " 的打卡任务\n")
files = open(os.getcwd() + "/main/day.txt", 'r+')
if files.read() == time.strftime("%Y/%m/%d"):
    print("今日已打卡")
    if os.path.exists(os.getcwd() + "/main/__pycache__/"):
        remove(os.getcwd() + "/main/__pycache__/")
    sys.exit()

# 读取用户列表
f2 = open(os.getcwd() + "/main/users.json", 'r', encoding='utf-8')
info = json.loads(f2.read())
f2.close()
text = '| 姓名 | 结果 |\n'
for i in range(len(info)):
    if info[i].get("enable") == 'true':
        name = info[i].get("name")
        print("开始为 " + name + " 打卡...")
        # 随机UA
        f = open(os.getcwd() + "/main/ua.txt", 'r', encoding='utf-8')
        num = f.read().split("\n")
        UA = num[random.randint(0, len(num) - 1)]
        f.close()
        try:
            # 如果用户(users.json)填写含有schoolcode则设为对应学校
            # 否则设为滁州学院（外校同学设置为自己学校domain编码）
            if "schoolcode" not in info[i]:
                info[i]['schoolcode'] = 'chzu'
            # 获取用户cookie
            cook = sign.login(info[i], UA)
            text += "| " + name + " | " + post.run(info[i]['schoolcode'], UA, cook) + " | \n"
        except Exception:
            print("---为 " + name + " 打卡失败\n")
            text += "| " + name + " | 打卡失败 | \n"

print("打卡结束\n")

try:
    qq(time.strftime("%Y年%m月%d日") + "\n自动打卡任务已完成", text + "\n[点我查看运行状况](https://github.com/xsk666/autopost/actions)")
except requests.exceptions.ConnectionError:
    print("推送qq通知出错")

# 更新day.txt
# 回到文件头部，清除重写
files.seek(0)
files.truncate()
files.write(time.strftime("%Y/%m/%d"))
files.close()
if os.path.exists(os.getcwd() + "/main/__pycache__/"):
    remove(os.getcwd() + "/main/__pycache__/")
