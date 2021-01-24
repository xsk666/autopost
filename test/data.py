# coding=utf-8
import sign
import json
import requests

# 读取用户列表
f = open("./users.json", 'r')
info = json.loads(f.read())
f.close()

# 获取昨天的记录


def log(stucode, password, name):
    UA = 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    cook = sign.login("2020211760", '123456', UA)
    url1 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code=chzu&stu_code=2020211760&authorityid=0&type=3&pagenum=1&pagesize=1000&stu_range=999&searchkey='
    head = {
        'Host': 'yq.weishao.com.cn',
        'User-Agent': UA,
        'Accept': '*/*',
        'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    private = json.loads(requests.get(url1, headers=head).text).get("data")[0]['private_id']
    url2 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code=chzu&stu_code=2020211760&activityid=5416&can_repeat=1&page_from=my&private_id=' + private
    response = requests.get(url2, headers=head).text
    ff = open("./data/" + name + ".json", "w", encoding="utf-8")
    ff.write(response)
    ff.close()


for i in range(0, len(info)):
    log(info[i].get("stucode"), info[i].get("password"), info[i].get("name"))
    print("ok")
