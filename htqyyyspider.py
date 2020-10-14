
import requests
import re
import time
songid=[]
songname=[]
headers={
		"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
		"Referer":"http://www.htqyy.com/top/hot",
		"Accept":"text/plain, */*; q=0.01"
		}

for i in range(0,2):
	url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
	html=requests.get(url,headers=headers).text
	pat1=r'title="(.*?)" sid'
	pat2=r'sid="(.*?)">'
	idlist=re.findall(pat2,html)
	titlelist=re.findall(pat1,html)
	songid.extend(idlist)
	songname.extend(titlelist)
	print(songname[6])

	
for i in range(0,len(songid)):
	headers={
	"Accept-Encoding":"identity;q=1, *;q=0",
	"Range":"bytes=3375104-",
	"Referer":"http://www.htqyy.com/play/"+str(songid[i]),
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
	}
	songurl="http://f2.htqyy.com/play8/"+str(songid[i])+"/mp3/8"

	date=requests.get(songurl,headers=headers).content
	print("正在下载",i+1,"首")
	with open(r"D:\pythontest\{}.mp3".format(songname[i]),"wb") as f:
		f.write(date)

	time.sleep(0.5)
	


