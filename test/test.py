# coding=utf-8
import json
import sign
import requests


def data(stucode, password, UA):
    cook = sign.login(stucode, password, UA)
    head4 = {
        'Host': 'yq.weishao.com.cn',
        'User-Agent': UA,
        'Accept': '*/*',
        'Referer': 'https://yq.weishao.com.cn/questionnaire',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    userinfo = json.loads(requests.get("https://yq.weishao.com.cn/userInfo", headers=head4).text).get("data")
    return {
        "sch_code": userinfo.get("schcode"),
        "stu_code": userinfo.get("stucode"),
        "stu_name": userinfo.get("username"),
        "identity": userinfo.get("identity"),
        "path": userinfo.get("path"),
        "organization": userinfo.get("organization"),
        "gender": userinfo.get("gender"),
        "activityid": "5416",
        "anonymous": 0,
        "canrepeat": 1,
        "repeat_range": 1, }


UA = 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
print(data("2020211760", "xu20021016", UA))
