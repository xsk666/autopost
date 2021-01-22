# coding=utf-8
import main
import json
import sign
import random

# 读取用户列表
f2 = open("./users.json", 'r', encoding='utf-8')
info = json.loads(f2.read())
for i in range(0, 1):
    # 获取用户cookie
    stucode = info[i].get("stucode")
    password = info[i].get("password")
    name=info[i].get("name")
    email = info[i].get("email")
    print("开始为 "+name+ " 打卡...")
    # 随机UA
    f = open("./ua.txt", 'r', encoding='utf-8')
    a = f.read().split("\n")
    UA = a[random.randint(0, len(a))]
    f.close()
    cook = sign.login(stucode, password,UA)
    main.run(name, stucode, password, email, UA, cook)

f2.close()




