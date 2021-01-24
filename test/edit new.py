# coding=utf-8
import requests
import sign
import json
f = open("./tzc.txt", 'r', encoding='utf-8')
info = f.read()
f.close()
UA = 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
stucode = '2020211899'
password = 'xu20021016'
cook = sign.login(stucode, password,UA)
# url 修改最新一条的打卡
url = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/editAnswer'
head = {
    'Host': 'yq.weishao.com.cn',
    'Connection': 'keep-alive',
    'User-Agent': UA,
    'Accept': '*/*',
    'Content-Length': str(len(info)),
    'Content-Type': 'application/json',
    'Origin': 'https://yq.weishao.com.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?edit=1&activityid=5416&page_from=onpublic&from_type=undefined&can_repeat=1&private_id=5416_1611299508403',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
}
# url1 提交今天的打卡
url1 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'

head1 = {
    'Host': 'yq.weishao.com.cn',
    'Connection': 'keep-alive',
    'User-Agent': UA,
    'Accept': '*/*',
    'Content-Length': str(len(info)),
    'Content-Type': 'application/json',
    'Origin': 'https://yq.weishao.com.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
}
print(requests.post(url, json=json.loads(info), headers=head).text)
