# coding=utf-8
import json
import os
import requests

# 读取用户列表
'''
f = open("./users.json", 'r')
info = json.loads(f.read())
for i in range(0, len(info)):
    print(str(info[i].get("stucode")+"\t"+info[i].get("password")))
f.close()
'''
# 读取所有支持微哨打卡的学校

f = open(os.getcwd()+"/学校列表.txt", 'a', encoding="utf-8")
info = json.loads(requests.get("https://api.weishao.com.cn/login/api/school").text).get("items")

for i in range(0, len(info)):
    f.write(info[i].get("name")+"\n")
    print(info[i].get("name"))

f.close()
