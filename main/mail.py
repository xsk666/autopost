# coding=utf-8
import requests


def qq(text, desp):
    return requests.get("https://qmsg.zendee.cn/send/4d762a772660e5bd2c725d1969633815?msg=" + text + "\n\n" + desp).json()
