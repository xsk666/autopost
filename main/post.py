# coding=utf-8
import requests
import getinfo


def run(studata,cook):
    """获取处理后的数据
    :param studatae:学生信息
    :param cook:传入的cookie
    :return :打卡结果
    """
    # 读取个人提交信息
    info = getinfo.data(studata, cook)
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
