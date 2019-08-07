#coding:utf-8
# 登录新浪微博
import os
import re
import time
import random
import json
import csv
# import cchardet
import requests
from lxml import etree

# 登录

params = {
	'accept': 'application/json, text/plain, */*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
	'cache-control': 'no-cache',
	'cookie': 'SCF=Ajm46vcFkuNkWmrTKOBYlUei4MMQ2uvG0oWzDRgupMJAdGr7IYBRutYbZt4RqUKLHptSMRiWiWe8GWO7uN8LhbQ.; _T_WM=1615bac0ac58aa55787de24de55202a5; SUB=_2A25xnqw-DeRhGeNI61cT-CrPzTWIHXVTYDR2rDV6PUJbkdAKLVnQkW1NSLtu_xUwNhxFTccMIQiHJMW4EgKNn0tj; SUHB=0xnygkOFFsXKan; SSOLoginState=1553652846; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4348619660537138%26luicode%3D20000061%26lfid%3D4348619660537138%26uicode%3D20000061%26fid%3D4348619660537138; XSRF-TOKEN=b601b1',
	'dnt': '1',
	'mweibo-pwa': '1',
	'pragma': 'no-cache',
	'referer': 'https://m.weibo.cn/detail/4348619660537138',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest',
	'x-xsrf-token': 'b601b1',
}

headers = {
	"Origin": "https://passport.weibo.cn",
	"Content-Length": "169", 
	"Accept-Language": "zh-CN,zh;q=0.8", 
	"Accept-Encoding": "gzip, deflate", 
	"Host": "passport.weibo.cn", 
	"Accept": "*/*", 
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", 
	"Connection": "keep-alive", 
	"Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=", 
	"Content-Type": "application/x-www-form-urlencoded"
}


def login(url,username,password):
	data = {
		"username": username, 
		"qq": "", 
		"savestate": "1", 
		"client_id": "", 
		"wentry": "", 
		"code": "", 
		"ec": "0", 
		"r": "http://weibo.cn/", 
		"loginfrom": "", 
		"hfp": "", 
		"pagerefer": "", 
		"entry": "mweibo", 
		"password": password, 
		"mainpageflag": "1", 
		"hff": ""
	}
	s=requests.Session()
	s.post(url,headers=headers,data=data)
	return s

def getComments(s = '', page = 0):
	content_url = 'https://m.weibo.cn/api/comments/show?id=4335581867294668&page='+str(page)
	r = s.get(content_url, headers = params)
	r.encoding = 'utf-8'
	content = r.text
	j = json.loads(content)
	print(j)
	print('*'*40)
	with open('data.txt', 'a+', encoding = 'utf-8') as f:
		f.write(str(j))

def main():
	login_url='https://passport.weibo.cn/sso/login'
	username='181####8751'
	password='s###a'

	web_url = 'https://m.weibo.cn/profile/info?uid=3847122978' # 网页版用户信息
	api_url = ''

	s = login(login_url,username,password)
	r = s.get(web_url, headers = params)
	r.encoding = 'utf-8'
	content = r.text
	
	exit()
	for i in range(0, 500):
		getComments(s,i)
		time.sleep(4)

	
if __name__ == '__main__':
	main()
