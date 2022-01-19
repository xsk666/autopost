# 每日健康打卡

[![每日打卡](https://github.com/xsk666/autopost/actions/workflows/test.yml/badge.svg?event=schedule)](https://github.com/xsk666/autopost/actions/workflows/test.yml)
<img alt="last commit" src="https://img.shields.io/github/last-commit/xsk666/autopost">
<img alt="Issues" src="https://img.shields.io/github/issues-closed/xsk666/autopost">
<img alt="Fork" src="https://img.shields.io/github/forks/xsk666/autopost">
<img alt="Star" src="https://img.shields.io/github/stars/xsk666/autopost">

![表情包](course/img/daka.jpeg)

## 使用教程/部署教程
***脚本会自动获取昨天的打卡信息进行提交***   
部署时请修改原有的个人信息(key和users.json)  
详见[`wiki`](https://github.com/xsk666/autopost/wiki)  
或者项目内的`course`内的[`readme.md`](/course/readme.md)

## 自述（一堆废话）

这是我第一次使用编写自动打卡的脚本  
我选择了`python`  
这也是我用`python`写的第一个项目   
并将它放在`github actions`上每日自动运行  
这也是我第一次使用`git`  
第一次编写文档 我选择了`Markdown`   
为了这个项目我花了很多时间学习  
恳请各位大佬给个 ***star***

## 使用范围

此项目理论上可用于200+所高校的每日打卡  
现可以直接在滁州学院使用  
***(外校使用的话，需要修改一些文件。详见[`wiki`](https://github.com/xsk666/autopost/wiki))***  
(外校同学若需要可以发issues联系我)  
(项目中含有个人数据，在***fork***之后请及时修改为你的数据)  
具体校园列表请看[`学校列表.txt`](/学校列表.txt)   
此学校列表由此得来-><https://api.weishao.com.cn/login/api/school>

(只要是基于`微哨`的应该都可以)

## 项目构成

简单介绍一下这个项目的构成
> 全部代码在[`main`](/main)文件夹中  
> 部署文档在[`course`](/course)

> 启动文件是[`index.py`](/main/index.py)  
> 用户数据是[`users.json`](/main/users.json)  
> 登陆模块是[`sign.py`](/main/sign.py)   
> 获取打卡数据是[`getinfo.py`](/main/getinfo.py)  
> 打卡程序是[`post.py`](/main/post.py)
---  
如果有`疑问`或`bug` 可以发[`issues`](https://github.com/xsk666/autopost/issues)  
此项目还在持续维护中...
