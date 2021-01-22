# coding=utf-8
import requests
import json
# 定义一些东西
api = 'api.weishao.com.cn'


def run(name, stucode, password, email, UA, cook):
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
    '''
    # 获取昨天的记录
    response = json.loads(requests.get(url1, headers=head).text).get("data")[0]['private_id']
    url2 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code=chzu&stu_code=2020211760&activityid=5416&can_repeat=1&page_from=my&private_id=' + response
    response = requests.get(url2, headers=head).text
    '''
    # 提交今日打卡
    url3 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
    # 读取个人提交信息
    f = open("./data.txt", 'r', encoding='utf-8')
    info = f.read()
    f.close()
    head1 = {
        'Host': 'yq.weishao.com.cn',
        'Connection': 'keep-alive',
        'User-Agent': UA,
        'Accept': '*/*',
        'Content-Length': str(len(info)),
        'Content-Type': 'application/json',
        'Origin': 'https://yq.weishao.com.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://yq.weishao.com.cn/questionnaire/addanswer?page_from=onpublic&activityid=5416&can_repeat=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
    }
    data = json.loads(requests.post(
        url3, json=json.loads(info), headers=head).text)
    if(data.get("data") == "提交成功"):
        print("打卡成功")
        mail.mail(email, name)
    if(data.get("errmsg") == "不能重复回答同一问卷"):
        print("今日打卡已完成，自动打卡取消")
