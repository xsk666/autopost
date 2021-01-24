# coding=utf-8
import requests
'''
url = 'https://yq.weishao.com.cn/check/questionnaire'
url2 = requests.get(url, allow_redirects=False).headers['Location']
print(url2)
response = requests.get(url2, allow_redirects=False)
print(response.headers['set-cookie'])
'''
url2 = "https://api.weishao.com.cn/login?source=%2Foauth%2Fauthorize%3Fclient_id%3DpqZ3wGM07i8R9mR3%26redirect_uri%3Dhttps%253A%252F%252Fyq.weishao.com.cn%252Fcheck%252Fquestionnaire%26response_type%3Dcode%26scope%3Dbase_api%26state%3Druijie"
url = "https://api.weishao.com.cn/oauth/authorize?client_id=pqZ3wGM07i8R9mR3&redirect_uri=https%3A%2F%2Fyq.weishao.com.cn%2Fcheck%2Fquestionnaire&response_type=code&scope=base_api&state=ruijie"
re = requests.get(url2).headers
print(re)
