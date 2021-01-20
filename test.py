# coding=utf-8
import requests
import time
req = requests.get('https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=测试时间&desp=github时间：' +
                   str(time.asctime(time.localtime(time.time()))))

