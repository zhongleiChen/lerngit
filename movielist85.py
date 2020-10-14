import requests
import re
import urllib.request
#爬取电话号码
'''
url="https://changyongdianhuahaoma.51240.com/"
headers={
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
	}
html=requests.get(url,headers=headers).text
pat1=re.compile(r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>(.*?)</td>')
phonelist=re.findall(pat1,html)

print(phonelist)
'''



#爬取豆瓣top250
'''headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
	}
movielist=[]
for i in range(0,2):
	url="http://movie.douban.com/top250?start="+str(50*i)+"&filter="
	request=urllib.request.Request(url,headers=headers)
	html=urllib.request.urlopen(request).read().decode()

	pat1=re.compile(r'<span class="title">(.*?)</span>[\s\S]*?<span class="title">&nbsp;/&nbsp')
	results=re.findall(pat1,html)
	movielist.extend(results)

print(movielist)
'''
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20