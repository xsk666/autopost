# coding=utf-8
import requests
import json
import mail
import getinfo


def run(user, UA, cook):
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
    # 提交今日打卡
    url3 = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
    # 读取个人提交信息
    info = getinfo.data(UA, cook)
    head1 = {
        'Host': 'yq.weishao.com.cn',
        'Connection': 'keep-alive',
        'User-Agent': UA,
        'Accept': '*/*',
        'Content-Length': str(len(str(info))),  # json转文字读取长度，再转为字符串
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
    data = json.loads(requests.post(url3, json=info, headers=head).text)
    print("服务器消息："+data.get("errmsg"))
    if(data.get("data") == "提交成功"):
        print("打卡成功！")
        if (user.get("notice") == "true"):
            print("正在发送邮件···")
            mail.send(user.get("email"), user.get("name"))

    elif(data.get("errcode") == 500):
        print("今日打卡已完成，自动打卡取消\n")
