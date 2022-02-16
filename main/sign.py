# coding=utf-8
import requests, re


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

    try:
        url = "https://xiaoyuan.weishao.com.cn"
        csrf_html = requests.get(f"{url}/login?path=%2Fhome")
        csrf = re.compile('(?<=value=")(.+)(?=">)').search(csrf_html.text)[0]
        data = {"domain": schoolcode, "stuNo": stucode, "pwd": password, "vc": "", "_csrf": csrf}
        cook = "locale=zh; " + re.compile("xiaoyuan=(.+)(?=; P)").search(csrf_html.headers['set-cookie'])[0]
        head = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cookie': cook,
        }
        res = requests.post(url + "/login/api/login", json=data, headers=head)
        errmsg = res.json().get("errmsg")
        if errmsg.find("错误") != -1:
            print(name + " " + errmsg)
            return "登录错误"
        cook2 = res.headers['set-cookie'].split(";")[0]

        head2 = {
            "Cookie": cook + "; " + cook2
        }
        res = requests.get(url + "/link?type=1&id=aa13361944680028&url=https%3A%2F%2Fyq.weishao.com.cn%2Fcheck%2Fquestionnaire", headers=head2,
                           allow_redirects=False).headers["location"]
        cook3 = requests.get(res, allow_redirects=False).headers['set-cookie'].split(";")[0] + ";" + cook2
        return cook3
    except requests.exceptions.ConnectionError as e:
        print("网络错误",e)
        return "网络错误"
    except KeyError:
        if retry:
            print(name + " 登录错误")
            return "登录错误"
        else:
            return login(user,True)
