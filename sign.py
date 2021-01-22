# coding=utf-8
import requests
import json
import time
import mail
stucode = '2020211760'
password = 'xu20021016'
# 登陆流程


def login(stucode, password, UA):
    api = 'api.weishao.com.cn'
    # 开始登陆
    url = 'https://yq.weishao.com.cn/check/questionnaire'
    url2 = requests.get(url, allow_redirects=False).headers['Location']
    response = requests.get(url2, allow_redirects=False)
    # 登陆cookie
    cook = response.headers['set-cookie']
    # 提交的个人数据
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
    response = requests.post(
        url3, data=dat, headers=head1, allow_redirects=False)
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
    return cook
