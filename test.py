# coding=utf-8
import requests
import json
import time
import mail,sign
stucode = '2020211760'
password = 'xu20021016'
# 登陆流程
api = 'api.weishao.com.cn'
UA = 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
cook = sign.login(stucode,'123456',UA)

head4 = {
    'Host': 'yq.weishao.com.cn',
    'User-Agent': UA,
    'Accept': '*/*',
    'Referer': 'https://yq.weishao.com.cn/questionnaire',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
}
# 获取身份信息
# 没用。。无用代码
#response = requests.get("https://yq.weishao.com.cn/userInfo", headers=head4)
# print(response.text)
#
# 没明白这个啥用
#  response = requests.get(
#    "https://yq.weishao.com.cn/api/questionnaire/questionnaire/getAuthList?domain=chzu&stu_code=2020211760&send_app_id=questionnaire&logic=1", headers=head3)
#authorityid = json.loads(response.text).get('data').get("data")
# url6 = "https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code=chzu&stu_code=2020211760&authorityid=" + \
#   authorityid+"&type=1&pagenum=1&pagesize=20&stu_range=999&searchkey="
#response = requests.get(url6, headers=head4)
# print(response.text)

url7 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code=chzu&stu_code=2020211760&authorityid=0&type=3&pagenum=1&pagesize=1000&stu_range=999&searchkey='
head5 = {
    'Host': 'yq.weishao.com.cn',
    'User-Agent': UA,
    'Accept': '*/*',
    'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
}
# 获取昨天的记录
response = json.loads(requests.get(url7, headers=head5).text).get("data")[
    0]['private_id']
url9 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code=chzu&stu_code=2020211760&activityid=5416&can_repeat=1&page_from=my&private_id=' + response
response = requests.get(url9, headers=head5).text
'''
f = open("./cookie.txt", 'w', encoding='utf-8')
f.write(response)
f.close()
'''
print(response)