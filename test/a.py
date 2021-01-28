# coding=utf-8
import requests,time
hapi = "https://api.weishao.com.cn"
api = 'lightapp.weishao.com.cn'
dat = "schoolcode=chzu&username=203135&password=Aa336699&verifyValue=&verifyKey=203135_chzu&ssokey="
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
url = 'https://lightapp.weishao.com.cn/check/reportstatistics'

url2 = requests.get(url, allow_redirects=False).headers['Location']
res = requests.get(url2, allow_redirects=False).headers
cook = res['set-cookie']
url3 = hapi + res['Location']
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
url4 = hapi + requests.post(url3, data=dat, headers=head, allow_redirects=False).headers['Location']

head2 = {
    'Host': api,
    'cache-control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': UA,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    "Cookie": cook
}
url5 = requests.get(url4, headers=head2, allow_redirects=False).headers['Location']
cookie = requests.get(url5, headers=head2, allow_redirects=False).headers['set-cookie']
print(cookie)
# 1001，1078，2508，3313
# 网工201:3313
# 网工202:3314
# 智能20:3320
urljiancha = "https://lightapp.weishao.com.cn/api/reportstatistics/reportstatistics/getStatistical"
data = {"type": "org", "identity": "", "para": {"organization_id": "3314", "organization_path_str": "3313,3314,3320"},
        "date": time.strftime("%Y-%m-%d"), "activityid": "5599", "flag": 0, "domain": "chzu", "stucode": "203135"}
