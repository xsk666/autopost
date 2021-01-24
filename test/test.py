# coding=utf-8
import json
import sign
import requests


def data(stucode, password, UA):
    cook = sign.login(stucode, password, UA)
    # 获取昨天的打卡信息
    url1 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code=chzu&stu_code=2020211760&authorityid=0&type=3&pagenum=1&pagesize=1000&stu_range=999&searchkey='
    head = {
        'Host': 'yq.weishao.com.cn',
        'User-Agent': UA,
        'Accept': '*/*',
        'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    private = json.loads(requests.get(url1, headers=head).text).get("data")[0]['private_id']
    url2 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code=chzu&stu_code=2020211760&activityid=5416&can_repeat=1&page_from=my&private_id=' + private
    # data里面存放着昨天的打卡记录
    data = json.loads(requests.get(url2, headers=head).text).get("data").get("question_list")
    # 但服务器返回的数据并不是真正提交的数据，需要处理
    # 下面开始处理昨天的记录
    # questions记录全部（包括未填写
    questions = []
    # questionsok记录填写的题目
    questionsok = []
    type1 = []
    type3 = []
    type7 = []
    type8 = []
    type9 = []

    for i in range(0, len(data)):
        # 1：选择题
        # 3：填空题
        # 7：定位
        # 8：填空题（不在校，所在省市）
        # 9：滑动选择题（返回时间）
        
        num = data[i].get("question_type")
        if (num == 1):
            print(data[i].get('questionid'))
            type1.append(data[i])
        elif (num == 3):
            type3.append(data[i])
        elif (num == 7):
            type7.append(data[i])
        elif (num == 8):
            type8.append(data[i])
        elif (num == 9):
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
            "answered": ''
        }
    for i in range(0, len(type1)):
        que = ques()
        opt = type1[i].get("option_list")
        for ii in range(0, len(opt)):
            if (str(opt[ii].get("optionid")) == type1[i].get("user_answer_optionid")):
                que['questionid'] = opt[ii].get("questionid")
                que["optionid"] = str(opt[ii].get("optionid"))
                que['optiontitle'] = opt[ii].get("title")
                que["question_type"] = type1[i].get("question_type")
                que["answered"] = str(type1[i].get("user_answer_this_question"))
                questions.append(que)
                break

    for i in range(0, len(type3)):
        que = ques()
        que['questionid'] = type3[i].get("questionid")
        que['question_type'] = type3[i].get("question_type")
        que['content'] = type3[i].get("user_answer_content")
        que["answered"] = str(type3[i].get("user_answer_this_question"))
        questions.append(que)

    for i in range(0, len(type7)):
        que = ques()
        que['questionid'] = type7[i].get("questionid")
        que['content'] = type7[i].get("user_answer_content")
        que['question_type'] = type7[i].get("question_type")
        que["answered"] = str(type7[i].get("user_answer_this_question"))
        questions.append(que)

    for i in range(0, len(type8)):
        que = ques()
        que['questionid'] = type8[i].get("questionid")
        que['content'] = type8[i].get("user_answer_content")
        que['question_type'] = type8[i].get("question_type")
        que['answered'] = type8[i].get("user_answer_this_question")
        que['hide'] = "true"
        que["answered"] = str(type8[i].get("user_answer_this_question"))
        questions.append(que)

    for i in range(0, len(type9)):
        que = ques()
        que['questionid'] = type9[i].get("questionid")
        que['question_type'] = type9[i].get("question_type")
        que['content'] = type9[i].get("user_answer_content")
        que['answered'] = type9[i].get("user_answer_this_question")
        que['hide'] = "true"
        que["answered"] = str(type9[i].get("user_answer_this_question"))
        questions.append(que)

    # 选择排序法
    for i in range(0, len(questions)-1):
        n = i
        for j in range(i + 1, len(questions)):
            if (int(questions[n].get('questionid')) > int(questions[j].get("questionid"))):
                n = j
        temp = questions[n]
        questions[n] = questions[i]
        questions[i] = temp

    for i in range(0, len(questions)):
        
        if (str(questions[i].get('answered')) == "True"):
            questions[i]["isanswered"] = "true"
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
    userinfo = json.loads(requests.get("https://yq.weishao.com.cn/userInfo", headers=head4).text).get("data")
    return {
        "sch_code": userinfo.get("schcode"),
        "stu_code": userinfo.get("stucode"),
        "stu_name": userinfo.get("username"),
        "identity": userinfo.get("identity"),
        "path": userinfo.get("path"),
        "organization": userinfo.get("organization"),
        "gender": userinfo.get("gender"),
        "activityid": "5416",
        "anonymous": '0',
        "canrepeat": '1',
        "repeat_range": '1',
        "question_data": questionsok,
        "totalArr": questions,
        "private_id": '0'
    }


UA = 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

a = data("2020211760", "xu20021016", UA)
f = open("./ok.json", 'w', encoding='utf-8')
json.dump(a, f, ensure_ascii=False)
f.close()
print('ok')
