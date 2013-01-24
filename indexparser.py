from urllib.request import urlopen
import re


def parseIndex(path):
	'''
	匹配类似 <a href="thread-5175-1-1.html">魔王DIY 10 － 第一百零二章 送人送到家</a> 这样的文本
	'''
	#indexpattern = re.compile('<a href="thread*>*</a>')
	indexpattern = re.compile('<a href="thread(.*)">魔王DIY (\d{2}) － (.*)</a>')
	with open(path) as indexfile:
		for a_line in indexfile:
			result = indexpattern.search(a_line)
			if result:
				#print(a_line)
				group = result.groups()
				print('thread' + group[0])
				print(group[1])
				print(group[2])
	print('end')


def readcontent(path, bookid, chaptername):
	contentPattern = re.compile('[^<](.*)<br />')
	contentPattern2 = re.compile('(</span>|^)(.*)(<br />|<span)')
	noDisplayPattern = re.compile('<span style="display:none;">(.*)</span>')
	noDisplayPattern2 = re.compile('<span style="font-size:0px;color:#E7F4FE;">(.*)</span>')
#	url = "http://bbs.yys5.com/" + path
#	response = urlopen(url)
	response = open(r'C:\Users\tong_zhengyu\Desktop\4.htm')
	for a_line in response:
		#l = a_line.decode('gbk')
		l = a_line
		#print(l)
		result = contentPattern2.search(l)
		if result:
			print(l)
			print(result.groups())

	#content = response.read().decode('gbk')
	#标题 </script></div><span style="color: navy; font: bold 12pt Arial, Tahoma; text-decoration: underline;">魔王DIY 01 － 第一章 昆仑魔王</span>
	#开头 <span style="font-family: '宋体', Arial, Tahoma; line-height: 160%">
	#结尾 </div>
	#每一行 <span style="display:none;">7.m(.P:.u8.l#.{*.r..E</span><span style="font-size:0px;color:#E7F4FE;">3.f-.~%.z9.J1.L7.D).}</span><br /> 中间无内容
	# 或 内容<br />
	#print(content)
	print('end')


if __name__ == '__main__':
	#parseIndex(r"C:\Users\tzycwf\Desktop\3.html")
	readcontent('thread-3243-1-3.html', '01', '第一章 昆仑魔王')
