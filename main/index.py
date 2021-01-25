# coding=utf-8
import main
import json
import sign
import random
import os
import requests
import time
print("开始 "+time.strftime("%Y/%m/%d")+" 的打卡任务")
#requests.get("https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=开始 "+time.strftime("%Y/%m/%d")+" 自动打卡任务&desp=[点我查看运行状况](https://github.com/xsk666/autopost/actions)")
# 读取用户列表
f2 = open(os.getcwd()+"/main/users.json", 'r', encoding='utf-8')
info = json.loads(f2.read())
f2.close()

for i in range(0, len(info)):
    print("开始为 "+info[i].get("name") + " 打卡...")
    # 随机UA
    f = open(os.getcwd()+"/main/ua.txt", 'r', encoding='utf-8')
    a = f.read().split("\n")
    UA = a[random.randint(0, len(a)-1)]
    f.close()
    # 获取用户cookie
    cook = sign.login(info[i], UA)
    main.run(info[i], UA, cook)
print("打卡结束")
