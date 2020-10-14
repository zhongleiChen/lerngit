import urllib.request
import urllib
import time


def loadpage(url,filename):
	print(filename+"正在下载")
	headers={
		"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
		"sec-fetch-site":"same-site",
		"sec-fetch-mode":"navigate",
		"referer":"https://bbs.hupu.com/all-gambia"
		}
	request=urllib.request.Request(url,headers=headers)
	return urllib.request.urlopen(request).read()


def writepage(html,filename):
	print(filename+"正在保存")
	with open(filename,"wb") as q:
		q.write(html)
		print("--------------------------------")
	


def hupuspider(url,beginpage,endpage):
	for page in range(beginpage,endpage+1):
		filename=r"D:\pythontest\第"+str(page)+"页.html"
		fullurl=url+"&page="+str(page)
		html=loadpage(fullurl,filename)
		writepage(html,filename)



if __name__ == '__main__':
	q=input("请输入搜索关键词")
	beginpage=int(input("请输入开始页码"))
	endpage=int(input("请输入结束页码"))
	url="https://my.hupu.com/search?"
	key=urllib.parse.urlencode({"q":q})
	fullurl=url+key
	hupuspider(fullurl,beginpage,endpage)


time.sleep(6)

















