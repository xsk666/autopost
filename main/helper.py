# coding=utf-8
import sys
import time

import requests

import post
import sign

hapi = "https://api.weishao.com.cn"
api = 'lightapp.weishao.com.cn'
dat = "schoolcode=chzu&username=203135&password=203135&verifyValue=&verifyKey=203135_chzu&ssokey="
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
url = 'https://lightapp.weishao.com.cn/check/reportstatistics'
oauth = "/oauth/authorize?client_id=pqZ3wGM07i8R9mR3&redirect_uri=https://lightapp.weishao.com.cn/check/reportstatistics&response_type=code&scope=base_api&state=ruijie"


def login():
    # 多次重定向后登录
    url2 = hapi + oauth
    cook = requests.get(url2, allow_redirects=False).headers['set-cookie']
    url3 = hapi + "/login?source=" + oauth
    head = {
        'Host': api,
        'cache-control': 'max-age=0',
        'Content-Length': '92',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'null',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        "Cookie": cook
    }
    # 登陆
    requests.post(url3, data=dat, headers=head, allow_redirects=False)
    head.pop('Content-Length')

    url5 = requests.get(url2, headers=head, allow_redirects=False).headers['Location']
    cook = "Hm_lvt_2897656ea377e58fb1af08554ed019b4=1611801447,1611805930,1611815687,1611818213;" + \
           requests.get(url5, headers=head, allow_redirects=False).headers['set-cookie'].split("; ")[0]
    return cook


try:
    cook = login()
except requests.exceptions.ConnectionError:
    print("登录错误")
    sys.exit()

nodaka = []  # 未打卡名单
url1 = "https://lightapp.weishao.com.cn/api/reportstatistics/reportstatistics/getStatistical"
data = {"type": "org", "identity": "", "para": {"organization_id": "3311,3312,3313,3314,3320", "organization_path_str": "3311,3312,3313,3314,3320"},
        "date": "2021-04-10", "activityid": "5599", "flag": 1, "domain": "chzu", "stucode": "203135"}
head = {
    'Host': api,
    'cache-control': 'max-age=0',
    'Content-Length': "217",
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/json',
    'User-Agent': UA,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    "Cookie": cook
}
list = requests.post(url1, json=data, headers=head).json().get("data").get("tree")
txt = ""
for i in range(0, len(list)):
    classes = list[i]
    data2 = {"type": "org", "identity": "", "para": {"organization_id": classes['unionid'], "organization_path_str": "3311,3312,3313,3314,3320"},
             "date": time.strftime("%Y-%m-%d"), "activityid": "5599", "flag": 0, "domain": "chzu", "stucode": "203135"}
    head['Content-Length'] = str(len(str(data2)))
    li = requests.post(url1, json=data2, headers=head).json().get("data")
    print(classes.get("tree_name"), str(li.get("orgUserCount") - li.get("reportCount")) + "人未打卡")
    if li.get("orgUserCount") != li.get("reportCount"):
        text = "| "
        for user in li.get("users"):
            if user.get("is_report") == 0:
                text += user.get("user_name") + " | "
                # 添加未打卡学生信息到列表
                nodaka.append({"stucode": user.get("user_id"), "password": user.get("user_id"), 'schoolcode': 'chzu'})
        print(text + "\n")
        txt += "{}   {}人未打卡\n{}".format(classes.get("tree_name"), li.get("orgUserCount") - li.get("reportCount"), text)
        if i != len(list) - 1:
            txt += "\n\n"
# qmsg酱推送到QQ
# requests.get("https://qmsg.zendee.cn/send/11a4ed5a314c66df757718ba36fea180?msg=" + txt).json()

if len(nodaka) == 0:
    print("所有人打卡完成")
    sys.exit()

for i in range(0, len(nodaka)):
    print("开始为 " + nodaka[i].get("stucode") + " 打卡")
    try:
        cook = sign.login(nodaka[i], UA)
        post.run(nodaka[i]['schoolcode'], UA, cook)
    except requests.exceptions.ConnectionError:
        print("---为 " + nodaka[i].get("stucode") + " 打卡失败")
print("\n所有人打卡完成")
