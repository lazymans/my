import httplib2
from xml.etree import ElementTree
import time

'''
Python Post 访问网络
'''


def postData(server, data):
	httplib2.debugLevel = 1
	h = httplib2.Http('.cache')	
	response, content = h.request(server, 
		'POST', 
		data, 
		headers={'Content-Type': 'application/x-www-form-urlencoded'})
	#print(content)
	return content

'''
Xml中查找节点
'''


def parseTaskInfo(responseText):
	root = ElementTree.fromstring(responseText)	
	statusNode = root.getiterator('Status')[0]
	if statusNode is not None:
		return statusNode.text
	else:
		return None

'''
智搜性能测试的框架
创建311/323IK/FZ分词的索引，分开创建
检查前一个创建索引的任务的执行情况，任务完成后才执行下一个任务
'''
if __name__ == '__main__':
	server311 = 'http://localhost:8091/fzsearch'
	server323 = 'http://localhost:8092/fzsearch'
	runTaskXml311 = '<?xml version="1.0"?><Command resource="Task" type="run"><Content><Name>Index-eBookFZ</Name></Content></Command>'

	runTask = r'g:\runTask.xml'
	getTask = r'g:\getTask.xml'
	print('>>>runTask 1...')
	with open(runTask, encoding='utf-8') as rT:
		postData(server1, rT.read())

	time.sleep(10)
	gT = open(getTask, encoding='utf-8')
	gtC = gT.read()
	gT.close()
	print('>>>getTask 1...')
	status = parseTaskInfo(postData(server1, gtC))
	while(status != '0'):
		print('>>>wait 20 Second...')
		time.sleep(20)
		status = parseTaskInfo(postData(server1, gtC))
	print('>>>Task 1 finish...')

	time.sleep(120)
	print('>>>runTask 2...')
	with open(runTask, encoding='utf-8') as rT:
		postData(server2, rT.read())

