# coding=gbk
import requests
import time
req = requests.get('https://sc.ftqq.com/SCU79675Tbfd23351bd3ed5501aae715beddfbdbf5e3a123f8fb98.send?text=github action测试&desp=github服务器时间' +
                   str(time.asctime(time.localtime(time.time()))))

