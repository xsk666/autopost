# coding=utf-8
import requests


def login(user, UA):
    stucode = str(user.get("stucode"))
    password = str(user.get("password"))
    # 学号，密码，UA
    api = 'api.weishao.com.cn'
    hapi = 'https://api.weishao.com.cn'
    # 分析协议得出的
    oauth = '/oauth/authorize?client_id=pqZ3wGM07i8R9mR3&redirect_uri=https%3A%2F%2Fyq.weishao.com.cn%2Fcheck%2Fquestionnaire&response_type=code&scope=base_api&state=ruijie'
    # 直接获取登陆链接的cookie（该链接极大可能是固定的）
    url = hapi + "/login?source=" + oauth
    # 得到初始cookie
    cook = requests.get(url).headers['set-cookie']
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

    requests.post(url, data=dat, headers=head1)
    url4 = hapi + oauth
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
    # 提交个人信息
    url5 = requests.get(url4, headers=head2, allow_redirects=False).headers['Location']
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
    # 登陆成功，获取登陆cookie
    cook = requests.get(url5, headers=head3, allow_redirects=False).headers['set-cookie']
    return cook
