from xml.etree import ElementTree
#from xml.dom import minidom

def parsexml():
	root = ElementTree.parse(r'g:\d.xml').getroot()
	contents = root.findall('content')
	#lID = [content.firstChild.wholeText for content in contents]
	
	for content in contents:
		try:			
			print(content.text)
		except :
			pass
	
	#return lID

if __name__ == '__main__':
	print(parsexml())

	