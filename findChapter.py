import os
import glob


dest = '</catalogRow>'
path = r'E:\TestSourceData\chapternew2\*_text.xml'


#list = glob.glob(path)
totalcount = 0
for f in glob.glob(path):
	#print(f)
	try:
		count = 0
		with open(f, encoding='utf-8') as a_file:
			for content in a_file:
				#content = a_file.read()
				#print(content)
				pos = 0
				pos = content.find(dest, pos)
				while pos >=0:
					count += 1
					pos = content.find(dest, pos+1)
		print(f, count)
		totalcount += count
	except:
		print('parse fail', f)


print('totalcount', totalcount)