# coding=utf-8
import requests


def login(user, UA):
    """获取处理后的数据
    :param user:用户信息
    :param UA:传入的UA
    :return : 传回登陆成功的cookie
    """
    # 学号，密码，学校编码，UA
    stucode = str(user.get("stucode"))
    password = str(user.get("password"))
    schoolcode = str(user.get("schoolcode"))

    api = 'https://api.weishao.com.cn'
    # 分析协议得出的
    oauth = '/oauth/authorize?client_id=pqZ3wGM07i8R9mR3&redirect_uri=https%3A%2F%2Fyq.weishao.com.cn%2Fcheck%2Fquestionnaire&response_type=code&scope=base_api&state=ruijie'
    # 直接获取登陆链接的cookie（该链接极大可能是固定的）
    url = api + "/login?source=" + oauth
    # 得到初始cookie
    cook = requests.get(url).headers['set-cookie']

    '''
       # 此处为备用登录，若登录失效，可将12-17行注释，然后启用此处再尝试登录
       # 从url开始，进行两次302跳转获取初始cookie和真正的登陆链接
       url = requests.get('https://yq.weishao.com.cn/check/questionnaire', allow_redirects=False).headers['Location']
       # 得到初始cookie
       cook = requests.get(url, allow_redirects=False).headers['set-cookie']
    '''

    # 提交的个人数据
    dat = "schoolcode=" + schoolcode + "&username=" + stucode + "&password=" + password + "&verifyValue=&verifyKey=" + stucode + "_" + schoolcode + "&ssokey="
    # 头部要携带提交的数据的长度
    head = {
        'Host': 'api.weishao.com.cn',
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
    # 提交个人信息（模拟登录）
    requests.post(url, data=dat, headers=head)
    # 修改headers
    head.pop("Content-Length")
    url4 = requests.get(api + oauth, headers=head, allow_redirects=False).headers['Location']
    # 修改headers
    head.pop("Cookie")
    # 登陆成功，获取登陆cookie
    cook = requests.get(url4, headers=head, allow_redirects=False).headers['set-cookie']
    return cook
