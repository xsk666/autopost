# -*- coding: utf8 -*-
import json
import os
import time
import requests
import re


def getdata(studata, cook):
    """获取处理后的数据

    :param studata:学生信息
    :param cook:传入的cookie
    :return : 昨天/上一次的打卡数据
    """
    # 只需要得到cookie即可获取信息
    schoolcode = studata.get("schoolcode")
    stucode = studata.get("stucode")
    url1 = f'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code={schoolcode}&stu_code={stucode}&authorityid=0&type=3&pagenum=1&pagesize=1000&stu_range=999&searchkey='
    head = {
        'Cookie': cook,
    }
    # 获取 昨天/最新 的打卡信息
    info = requests.get(url1, headers=head).json().get("data")[0]
    # 如果今天已完成打卡
    if info.get("createtime") == time.strftime("%Y-%m-%d"):
        return 0
    private = info['private_id']
    activityid = str(info["activityid"])
    url2 = f'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code={schoolcode}&stu_code={schoolcode}&activityid={activityid}&can_repeat=1&page_from=my&private_id={private}'
    # info里面存放着最新的的打卡记录
    info = requests.get(url2, headers=head).json().get("data")
    questions = info.get("question_list")
    private_id = info.get("last_private_id")
    flag = 0
    answers = []

    while flag < len(questions):
        answer = {
            "questionid": questions[flag].get("questionid"),
            "optionid": questions[flag].get("user_answer_optionid"),
            "optiontitle": 0,
            "question_sort": 0,
            'question_type': questions[flag].get("question_type"),
            "option_sort": 0,
            'range_value': "",
            "content": questions[flag].get("user_answer_content"),
            "isotheroption": questions[flag].get("otheroption"),
            "otheroption_content": questions[flag].get("user_answer_otheroption_content"),
            "isanswered": questions[flag].get("user_answer_this_question"),
            "answerid": questions[flag].get("answerid"),
        }
        jump = 0
        type = answer["question_type"]

        if type == 1:
            for i in questions[flag].get("option_list"):
                if answer["optionid"].isdigit() and i.get("optionid") == int(answer["optionid"]):
                    answer["optiontitle"] = i.get("title")
                    if questions[flag].get("hsjump"):
                        jump = i.get("jumpid") - 1

        elif type in [3, 4, 7, 8, 9]:
            answer["optionid"] = 0
        answer["answered"] = answer["isanswered"]
        answers.append(answer)
        if jump:
            flag = jump
        else:
            flag += 1

    flag = 0
    totalArr = []
    while flag < len(questions):
        answer = {
            "questionid": questions[flag].get("questionid"),
            "optionid": questions[flag].get("user_answer_optionid"),
            "optiontitle": 0,
            "question_sort": 0,
            'question_type': questions[flag].get("question_type"),
            "option_sort": 0,
            'range_value': "",
            "content": questions[flag].get("user_answer_content"),
            "isotheroption": questions[flag].get("otheroption"),
            "otheroption_content": questions[flag].get("user_answer_otheroption_content"),
            "isanswered": questions[flag].get("user_answer_this_question")
        }
        type = answer['question_type']

        if type == 1 and answer["optionid"] != "":
            for i in questions[flag].get("option_list"):
                if answer["optionid"].isdigit() and i.get("optionid") == int(answer["optionid"]):
                    answer["optiontitle"] = i.get("title")
        elif type in [3, 4, 7, 8, 9]:
            answer["optionid"] = 0

        if questions[flag].get("user_answer_this_question"):
            answer["isanswered"] = True
            answer["answerid"] = questions[flag].get("answerid")
            answer["answered"] = answer["isanswered"]
        else:
            answer["hide"] = True
            answer["optionid"] = 0
            answer["isanswered"] = ''
            answer["answered"] = False

        totalArr.append(answer)
        flag += 1

    head['Referer'] = 'https://yq.weishao.com.cn/questionnaire'
    userinfo = requests.get("https://yq.weishao.com.cn/userInfo", headers=head).json().get("data")
    data = {
        "sch_code": userinfo.get("schcode"),
        "stu_code": userinfo.get("stucode"),
        "stu_name": userinfo.get("username"),
        "identity": userinfo.get("identity"),
        "path": userinfo.get("path"),
        "organization": userinfo.get("organization"),
        "gender": userinfo.get("gender"),
        "activityid": activityid,
        "anonymous": 0,
        "canrepeat": 1,
        "repeat_range": 1,
        "question_data": answers,
        "totalArr": totalArr,
        "private_id": private_id
    }
    return data


def run(studata, cook):
    """获取处理后的数据
    :param studatae:学生信息
    :param cook:传入的cookie
    :return :打卡结果
    """
    # 读取个人提交信息
    info = getdata(studata, cook)
    if info == 0:
        print("今日打卡已完成，自动打卡取消\n")
        return "已完成"
    # 提交今日打卡
    url = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
    head = {
        'Content-Type': 'application/json',
        'Cookie': cook,
    }
    data = requests.post(url, json=info, headers=head).json()
    if data.get("errcode") == 0:
        print("打卡成功！")
        return "成功！"
    else:
        print("---未知的errcode\n" + str(data) + "\n")
        return "未知结果"


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
        print("网络错误", e)
        return "网络错误"
    except KeyError:
        if retry:
            print(name + " 登录错误")
            return "登录错误"
        else:
            return login(user, True)


def main_handler(event, context):
    print("开始 " + time.strftime("%Y/%m/%d") + " 的打卡任务\n")
    # 读取用户列表
    path = os.getcwd()
    if path.find("main") == -1:
        path += "/main"
    allinfo = json.load(open(path + "/users2.json", encoding="utf-8"))
    text = '| 姓名 |  结果  |'
    for item in allinfo:
        name = item.get("name")
        print("开始为 " + name + " 打卡...")

        try:
            # 获取用户cookie
            cook = login(item)
            if cook.find("错误") != -1:
                raise Exception(cook)
            # 获取返回的打卡结果
            response = run(item, cook)
        except Exception as e:
            print("---为 " + name + " 打卡失败\n" + str(e))
            response = "打卡失败"
        # 为推送填写打卡信息
        text += f" \n| {name} | {response} |"

    print("打卡结束\n")

    try:
        qmsg = "你的key"
        requests.get("https://qmsg.zendee.cn/send/" + qmsg + f'?msg={time.strftime("%Y年%m月%d日")}\n自动打卡任务已完成\n\n' + text).json()
    except:
        print("推送qq通知出错")


if __name__ == "__main__":
    main_handler("", "")
