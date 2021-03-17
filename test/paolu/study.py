# coding=utf-8
import requests

userInfo = 'http://dxx.ahyouth.org.cn/api/userInfo'
learn = 'http://dxx.ahyouth.org.cn/api/newLearn'
head1 = {
    'Host': 'dxx.ahyouth.org.cn',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/4747 ',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'token': 'riPObGOJKPPS4fFu1hvpvRFk5oDgpVGN',
    'Content-Type': 'application/json',
    'Referer': 'http://dxx.ahyouth.org.cn/',
    'X-Requested-With': 'com.tencent.mm',
    'Cookie': 'PHPSESSID=857160ee6000aa7493839c8cfc2cb554'
}
res = requests.post(userInfo , headers=head1, allow_redirects=False)
print(res.json())
