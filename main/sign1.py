# coding=utf-8
import requests
from urllib.parse import quote

def login(user, retry=False):
    """获取处理后的数据
    :param user:用户信息
    :return : 传回登陆成功的cookie
    """
    # 姓名，学号，密码，学校编码
    name = user.get("name")
    stucode = user.get("stucode")
    password = user.get("password")
    schoolcode = user.get("schoolcode")
    if schoolcode is None:
        print("未填写schoolcode")
        return "配置错误"
    api = 'https://api.weishao.com.cn'
    # 分析协议得出的
    oauth = '/oauth/authorize?client_id=pqZ3wGM07i8R9mR3&redirect_uri=https%3A%2F%2Fyq.weishao.com.cn%2Fcheck%2Fquestionnaire&response_type=code&scope=base_api&state=ruijie'
    # 直接获取登陆链接的cookie（该链接是固定的）
    url = api + "/login?source=" + oauth
    try:
        # 得到初始cookie
        session = requests.Session()
        cook = session.get(url).headers['set-cookie']
        # 提交的个人数据
        dat = "schoolcode=" + schoolcode + "&username=" + stucode + "&password=" + quote(password, "utf-8") + "&verifyValue=&verifyKey=" + stucode + "_" + schoolcode + "&ssokey="
        head = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cook,
        }
        # 提交个人信息（模拟登录）
        session.post(url, data=dat, headers=head)
        url1 = session.get(api + oauth, headers=head, allow_redirects=False).headers['Location']
        # 登陆成功，获取登陆cookie
        cook = session.get(url1, headers=head, allow_redirects=False).headers['set-cookie']
        return cook
    except requests.exceptions.ConnectionError:
        print("网络错误")
        return "网络错误"
    except requests.exceptions.MissingSchema:
        print("密码错误")
        return "密码错误"
    except:
        if retry:
            print(name + " 登录错误")
            return "登录错误"
        else:
            return login(user, True)
