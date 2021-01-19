import requests,json
url = 'https://yq.weishao.com.cn/check/questionnaire'
response = requests.get(url, allow_redirects=False)
url2 = response.headers['Location']
response = requests.get(url2, allow_redirects=False)
cook = response.headers['set-cookie']
head1 = {
    'Host': 'api.weishao.com.cn',
    'Content-Length': '102',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
    'X-Requested-With': 'mark.via'}

url3 = "https://api.weishao.com.cn" + response.headers['Location']
dat1 = "schoolcode=chzu&username=2020211760&password=xu20021016&verifyValue=&verifyKey=2020211760_chzu&ssokey="
response = requests.post(url3, data=dat1, headers=head1, allow_redirects=False)
url4 = "https://api.weishao.com.cn" + response.headers['Location']
head2 = {
    'Host': 'api.weishao.com.cn',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
    'X-Requested-With': 'mark.via'
}
response = requests.get(url4, headers=head2, allow_redirects=False)
url5 = response.headers['Location']
head3 = {
    'Host': 'api.weishao.com.cn',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'null',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'X-Requested-With': 'mark.via'
}
response = requests.get(url5, headers=head3, allow_redirects=False)
cook = response.headers['set-cookie']
head3 = {
    'Host': 'yq.weishao.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://yq.weishao.com.cn/questionnaire',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cookie': cook,
    'X-Requested-With': 'mark.via'}

##response = requests.get("https://yq.weishao.com.cn/userInfo", headers=head3)
##print(response.text)
response = requests.get("https://yq.weishao.com.cn/api/questionnaire/questionnaire/getAuthList?domain=chzu&stu_code=2020211760&send_app_id=questionnaire&logic=1",headers=head3)
authorityid = json.loads(response.text).get('data').get("data")
url6 = "https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code=chzu&stu_code=2020211760&authorityid="+authorityid+"&type=1&pagenum=1&pagesize=20&stu_range=999&searchkey="
response = requests.get(url6, headers=head3)
print(response.text)


def tijiao(cook):
    info = ''
    
    head4 = {
        'Host': 'yq.weishao.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'https://yq.weishao.com.cn/questionnaire',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cookie': cook,
        'X-Requested-With': 'mark.via'
    }
    r = requests.get('https: // yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer')
