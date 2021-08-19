# coding=utf-8
import json
import os
import random
import time
from shutil import rmtree as remove

import requests

import post
import sign


def qq(text, desp):
    qmsg = "你的key"
    return requests.get("https://qmsg.zendee.cn/send/" + qmsg + "?msg=" + text + "\n\n" + desp).json()


if __name__ == '__main__':
    print("开始 " + time.strftime("%Y/%m/%d") + " 的打卡任务\n")
    # 读取用户列表
    with open(os.getcwd() + "/users.json", 'r', encoding='utf-8') as file:
        allinfo = json.loads(file.read())
    with open(os.getcwd() + "/ua.txt", 'r', encoding='utf-8') as file:
        allUA = file.read().split("\n")
    text = '| 姓名 |  结果  |'
    for item in allinfo:
        name = item.get("name")
        print("开始为 " + name + " 打卡...")
        # 随机UA
        UA = random.choice(allUA)
        try:
            # 获取用户cookie
            cook = sign.login(item, UA)
            # 获取返回的打卡结果
            response = post.run(item, UA, cook)
        except Exception as e:
            print("---为 " + name + " 打卡失败\n" + str(e))
            response = "打卡失败"
        # 为推送填写打卡信息
        text += f" \n| {name} | {response} |"

    print("打卡结束\n")

    try:
        qq(time.strftime("%Y年%m月%d日") + "\n自动打卡任务已完成", text + "\n[点我查看运行状况](https://github.com/xsk666/autopost/actions)")
    except requests.exceptions.ConnectionError:
        print("推送qq通知出错")
