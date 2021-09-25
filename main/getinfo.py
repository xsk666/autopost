# coding=utf-8
import time
import requests


def data(studata, cook):
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
