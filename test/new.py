# coding=utf-8
import json
import os
f = open(os.getcwd()+"/data/xsk.json", "r", encoding="utf-8")
data = json.loads(f.read()).get("data").get("question_list")
f.close()
questions = []
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
        type1.append(data[i])
    elif (num == 3):
        type3.append(data[i])
    elif (num == 7):
        type7.append(data[i])
    elif (num == 8):
        type8.append(data[i])
    elif (num == 9):
        type9.append(data[i])

for i in range(0, len(type1)):
    que = {
        "questionid": '0',
        "optionid": "0",
        "optiontitle": "",
        "question_sort": '0',
        "question_type": '1',
        "option_sort": '0',
        "range_value": "",
        "content": "",
        "isotheroption": '0',
        "otheroption_content": "",
        "isanswered": 'true',
        "answerid": '0',
        "answered": 'true'
    }
    opt = type1[i].get("option_list")
    for ii in range(0, len(opt)):
        if (str(opt[ii].get("optionid")) == type1[i].get("user_answer_optionid")):
            que['questionid'] = opt[ii].get("questionid")
            que["optionid"] = opt[ii].get("optionid")
            que['optiontitle'] = opt[ii].get("title")
            que["question_type"] = type1[i].get("question_type")
            questions.append(que)
            break

for i in range(0, len(type3)):
    que = {
        "questionid": '0',
        "optionid": "0",
        "optiontitle": "",
        "question_sort": '0',
        "question_type": '1',
        "option_sort": '0',
        "range_value": "",
        "content": "",
        "isotheroption": '0',
        "otheroption_content": "",
        "isanswered": 'true',
        "answerid": '0',
        "answered": 'true'
    }
    que['questionid'] = type3[i].get("questionid")
    que['question_type'] = type3[i].get("question_type")
    que['content'] = type3[i].get("user_answer_content")
    questions.append(que)

for i in range(0, len(type7)):
    que = {
        "questionid": '0',
        "optionid": "0",
        "optiontitle": "",
        "question_sort": '0',
        "question_type": '1',
        "option_sort": '0',
        "range_value": "",
        "content": "",
        "isotheroption": '0',
        "otheroption_content": "",
        "isanswered": 'true',
        "answerid": '0',
        "answered": 'true'
    }
    
    que['questionid'] = type3[i].get("questionid")
    que['content'] = type3[i].get("user_answer_content")
    que['question_type'] = type3[i].get("question_type")
    questions.append(que)
    
for i in range(0, len(type8)):
    que = {
        "questionid": '0',
        "optionid": "0",
        "optiontitle": "",
        "question_sort": '0',
        "question_type": '1',
        "option_sort": '0',
        "range_value": "",
        "content": "",
        "isotheroption": '0',
        "otheroption_content": "",
        "isanswered": 'true',
        "answerid": '0',
        "answered": 'true'
    }
    que['questionid'] = type8[i].get("questionid")
    que['question_type'] = type8[i].get("question_type")
    que['answered'] = str(type8[i].get("user_answer_this_question"))
    que['hide'] = "true"
    que['isanswered'] = ""
    questions.append(que)

for i in range(0, len(type9)):
    que = {
        "questionid": '0',
        "optionid": "0",
        "optiontitle": "",
        "question_sort": '0',
        "question_type": '1',
        "option_sort": '0',
        "range_value": "",
        "content": "",
        "isotheroption": '0',
        "otheroption_content": "",
        "isanswered": 'true',
        "answerid": '0',
        "answered": 'true'
    }
    que['questionid'] = type9[i].get("questionid")
    que['question_type'] = type9[i].get("question_type")
    que['answered'] = str(type9[i].get("user_answer_this_question"))
    que['hide'] = "true"
    que['isanswered'] = ""
    questions.append(que)
#选择排序法

for i in range(0, len(questions)-1):
    n = i
    for j in range(i + 1, len(questions)):
        if (int(questions[n].get('questionid')) > int(questions[j].get("questionid"))):
            n = j
    temp = questions[n]
    questions[n] = questions[i]
    questions[i] = temp
