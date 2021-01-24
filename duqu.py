#coding=utf-8
import json
f = open("./data/xsk.json", 'r', encoding='utf-8')
info = json.loads(f.read()).get("data").get("question_list")
f.close()
for i in range(0, len(info)):
    optlist = info[i].get("option_list")
    for ii in range(0, len(optlist)):
        if(str(optlist[ii].get("optionid")) == info[i].get("user_answer_optionid")):
            print(str(i+1)+":\t"+str(info[i].get("questionid"))+"\t"+info[i].get("question_title") + ':\t' + optlist[ii].get("title"))
            break

#读取用户列表
'''
f = open("./users.json", 'r')
info = json.loads(f.read())
for i in range(0, len(info)):
    print(str(info[i].get("stucode")+"\t"+info[i].get("password")))
f.close()
'''
#读取所有支持微哨打卡的学校
'''
ff = open("../xx.txt", 'a', encoding="utf-8")
f = open("D:/xsk/Documents/Tencent Files/3104182180/FileRecv/MobileFile/xx(1).txt",
         "r", encoding='utf-8')
info = json.loads(f.read()).get("items")
for i in range(0, len(info)):
    ff.write(info[i].get("name")+"\n")
# print(info)
f.close()
ff.close()
'''
