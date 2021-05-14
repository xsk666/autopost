# coding=utf-8
import time

import requests


def data(studata, UA, cook):
    """获取处理后的数据
    :param studata:学生信息
    :param UA:传入的UA
    :param cook:传入的cookie
    :return : 昨天/上一次的打卡数据
    """
    # 只需要得到cookie即可获取信息
    # 获取 昨天/最新 的打卡信息
    schoolcode = studata.get("schoolcode")
    stucode = studata.get("stucode")
    url1 = f'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code={schoolcode}&stu_code={stucode}&authorityid=0&type=3&pagenum=1&pagesize=1000&stu_range=999&searchkey='
    head = {
        'Host': 'yq.weishao.com.cn',
        'User-Agent': UA,
        'Accept': '*/*',
        'Referer': 'https://yq.weishao.com.cn/questionnaire/my/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    info = requests.get(url1, headers=head).json().get("data")[0]
    if info.get("createtime") == time.strftime("%Y-%m-%d"):
        return 0
    private = info['private_id']
    activityid = str(info["activityid"])
    url2 = f'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code={schoolcode}&stu_code={schoolcode}&activityid=' + activityid + '&can_repeat=1&page_from=my&private_id=' + private
    # data里面存放着最新的的打卡记录
    data = requests.get(url2, headers=head).json().get("data")
    true = data.get('already_answered')  # 存放true
    false = data.get("can_reanswer")  # 存放false
    data = data.get("question_list")
    # 但服务器返回的数据并不是真正提交的数据，需要处理
    # 下面开始处理昨天的记录
    # questions记录全部（包括未填写
    questions = []
    # questionsok记录昨天填写的题目
    questionsok = []
    type1 = []
    type3 = []
    type4 = []
    type7 = []
    type8 = []
    type9 = []

    for i in range(len(data)):
        # 1：选择题
        # 3：填空题
        # 7：定位
        # 8：填空题（不在校，所在省市）
        # 9：滑动选择题（返回时间）
        num = data[i].get("question_type")
        if num == 1:
            type1.append(data[i])
        elif num == 3:
            type3.append(data[i])
        elif num == 4:
            type4.append(data[i])
        elif num == 7:
            type7.append(data[i])
        elif num == 8:
            type8.append(data[i])
        elif num == 9:
            type9.append(data[i])

    def ques():
        return {
            "questionid": '0',
            "optionid": 0,
            "optiontitle": 0,
            "question_sort": 0,
            "question_type": 1,
            "option_sort": 0,
            "range_value": "",
            "content": "",
            "isotheroption": 0,
            "otheroption_content": "",
            "isanswered": "",
            "answerid": 0,
            "hide": false,
            "answered": ''
        }

    for i in range(len(type1)):
        que = ques()
        opt = type1[i].get("option_list")

        if str(type1[i].get("user_answer_this_question")) == 'False':
            que['questionid'] = type1[i].get("questionid")
            que["question_type"] = type1[i].get("question_type")

        else:
            for ii in range(len(opt)):
                if str(opt[ii].get("optionid")) == type1[i].get("user_answer_optionid"):
                    que['questionid'] = opt[ii].get("questionid")
                    que["optionid"] = opt[ii].get("optionid")
                    que['optiontitle'] = opt[ii].get("title")
                    que["question_type"] = type1[i].get("question_type")
                    break
        que["answered"] = type1[i].get("user_answer_this_question")
        if que["answered"] == false:
            que["hide"] = true
        questions.append(que)

    for i in range(len(type3)):
        que = ques()
        que['questionid'] = type3[i].get("questionid")
        que['question_type'] = type3[i].get("question_type")
        que['content'] = type3[i].get("user_answer_content")
        que["answered"] = type3[i].get("user_answer_this_question")
        que["hide"] = true
        questions.append(que)

    for i in range(len(type4)):
        que = ques()
        que['questionid'] = type4[i].get("questionid")
        que['question_type'] = type4[i].get("question_type")
        que['content'] = type4[i].get("user_answer_content")
        que["answered"] = type4[i].get("user_answer_this_question")
        if que["answered"] == false:
            que["hide"] = true
        questions.append(que)

    for i in range(len(type7)):
        que = ques()
        que['questionid'] = type7[i].get("questionid")
        que['content'] = type7[i].get("user_answer_content")
        que['question_type'] = type7[i].get("question_type")
        que["answered"] = type7[i].get("user_answer_this_question")
        questions.append(que)

    for i in range(len(type8)):
        que = ques()
        que['questionid'] = type8[i].get("questionid")
        que['content'] = type8[i].get("user_answer_content")
        que['question_type'] = type8[i].get("question_type")
        que['answered'] = type8[i].get("user_answer_this_question")
        que["hide"] = true
        questions.append(que)

    for i in range(len(type9)):
        que = ques()
        que['questionid'] = type9[i].get("questionid")
        que['question_type'] = type9[i].get("question_type")
        que['content'] = type9[i].get("user_answer_content")
        que['answered'] = type9[i].get("user_answer_this_question")
        que["hide"] = true
        questions.append(que)

    # 选择排序法
    for i in range(len(questions) - 1):
        n = i
        for j in range(i + 1, len(questions)):
            if int(questions[n].get('questionid')) > int(questions[j].get("questionid")):
                n = j
        temp = questions[n]
        questions[n] = questions[i]
        questions[i] = temp

    for i in range(len(questions)):
        if questions[i].get("questionid") == 61838:
            del questions[i]["hide"]
        if str(questions[i].get('answered')) == "True":
            questions[i]["isanswered"] = true
            questionsok.append(questions[i])

    head4 = {
        'Host': 'yq.weishao.com.cn',
        'User-Agent': UA,
        'Accept': '*/*',
        'Referer': 'https://yq.weishao.com.cn/questionnaire',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    userinfo = requests.get("https://yq.weishao.com.cn/userInfo", headers=head4).json().get("data")
    return {
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
        "question_data": questionsok,
        "totalArr": questions,
        "private_id": 0
    }
