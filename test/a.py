#coding=utf-8
import os,json
import sign
import getinfo
user = {
    "name": "xsk",
    "stucode": "20202118760",
    "password": "xu20021016",
    "email": "3104182180@qq.com",
    "notice": "true"
}

UA = 'Dalvik/2.1.0 (Linux; U; Android 9; SM-G3609 Build/KTU84P)'
cook = sign.login(user, UA)
data = getinfo.data(UA, cook)
f = open(os.getcwd() + "/data/test.json", "w", encoding="utf-8")
json.dump(data,f,ensure_ascii=False)
f.close()


print("ok")
