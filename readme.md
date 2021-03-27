# 每日健康打卡

## 自述（一堆废话）
这是我第一次使用编写自动打卡的脚本  
我选择了`python`  
这也是我用`python`写的第一个项目   
并将它放在`github actions`上每日自动运行  
这也是我第一次使用`git`  
第一次编写文档
我选择了`Markdown`   
为了这个项目我花了很多时间学习  
恳请各位大佬给个 ***star***  
***fork*** 后修改[`users.json`](/main/users.json)  
然后开启[`github actions`](https://github.com/xsk666/autopost/actions)就可以使用啦  


## 使用范围  
此项目可用于200+所高校的每日打卡  
但需要修改一些文件。  
***(现仅可以在滁州学院使用)***   
(项目中含有个人数据，为了`github actions`懒得修改了)  
(外校同学若需要可以发issues联系我)  
  
具体校园列表请看[`学校列表.txt`](/学校列表.txt)   
此学校列表由此得来-><https://api.weishao.com.cn/login/api/school>
  
(只要是基于`微哨`的应该都可以)

## 项目构成  
下面简单介绍一下这个项目的构成  
> 全部代码在[`main`](/main)文件夹中
>> [`test`](/test)文件夹是我正在进行的测试(与现有代码无关)  
> > 主要是因为我太菜了，还懒，所以就放在一起了

> 启动文件是[`index.py`](/main/index.py)  
> 用户数据是[`users.json`](/main/users.json)  
> 登陆模块是[`sign.py`](/main/sign.py)   
> 备用登陆模块是[`sign1.py`](/main/sign1.py)  
> 获取打卡数据是[`getinfo.py`](/main/getinfo.py)  
> 主程序是[`main.py`](/main/main.py)  
> 推送通知[`mail.py`](/main/mail.py)
>> 长期使用mail模块推送打卡成功通知后，发现QQ会警告(传播垃圾/骚扰信息)并禁止用户使用邮箱授权码推送邮件
---  
如果有`疑问`或`bug` 可以发[`issues`](https://github.com/xsk666/autopost/issues)  
此项目还在持续更新中...