# coding=utf-8
import requests
import json
import time
stucode = '2020211760'
password = 'xu20021016'
# 登陆流程
api = 'api.weishao.com.cn'
UA = 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
url = 'https://yq.weishao.com.cn/check/questionnaire'
url2 = requests.get(url, allow_redirects=False).headers['Location']
response = requests.get(url2, allow_redirects=False)
# 登陆cookie
cook = response.headers['set-cookie']
#提交的个人数据
dat = "schoolcode=chzu&username="+stucode+"&password=" + \
    password+"&verifyValue=&verifyKey="+stucode+"_chzu&ssokey="
# 头部要携带提交的数据的长度
head1 = {
    'Host': api,
    'Content-Length': str(len(dat)),
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': UA,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
}

url3 = "https://"+api + response.headers['Location']
response = requests.post(url3, data=dat, headers=head1, allow_redirects=False)
url4 = "https://"+api + response.headers['Location']
head2 = {
    'Host': api,
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': UA,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,

}
response = requests.get(url4, headers=head2, allow_redirects=False)
url5 = response.headers['Location']
head3 = {
    'Host': api,
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': UA,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',

}
response = requests.get(url5, headers=head3, allow_redirects=False)
# 登陆成功，获取登陆cookie
cook = response.headers['set-cookie']

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
#print(response.text)
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
#获取昨天的记录
response = json.loads(requests.get(url7, headers=head5).text).get("data")[0]['private_id']
url9 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code=chzu&stu_code=2020211760&activityid=5416&can_repeat=1&page_from=my&private_id=' + response
response = requests.get(url9, headers=head5).text
'''
f = open("./cookie.txt", 'w', encoding='utf-8')
f.write(response)
f.close()
'''

f = open("./data.json", 'r',encoding='utf-8')
info=f.read()
f.close()
head6 = {
    'Host': 'yq.weishao.com.cn',
    'User-Agent': UA,
    'Accept': '*/*',
    'Content-Length': str(len(info)),
    'Content-Type': 'application/json',
    'Origin': 'https://yq.weishao.com.cn',
    'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
}
url8 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
response = requests.post(url8, data=json.loads(
    info), headers=head6, allow_redirects=False).text
print(response)
if (json.loads(response).get("data") == '提交成功'):
    re=requests.get('https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=打卡成功&desp=时间：' +
                 str(time.asctime(time.localtime(time.time()))))
    if (json.loads(re.text).get("errmsg") == 'success'):
        print("OK")
