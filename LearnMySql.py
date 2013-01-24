'''
def CreateTable():
	pass

def search():
	pass
'''

import mysql.connector
connectInfo = {'user':'dev',
'password':'danzai',
'host':'127.0.0.1',
'database':'world'}

cnx = mysql.connector.connect(user='dev', password='danzai', host='127.0.0.1', database='world')

citylist = []
cursor = cnx.cursor()
query = ("SELECT name FROM city where countrycode='chn'")
cursor.execute(query)
for (city,) in cursor:
	try:
		#print(city)
		citylist.append(city)
	except :
		print("can't print city")

print('end of first result')
print(len(citylist))

populationList = []
queryPopulation = ("SELECT population FROM city where name = %s")
for city in citylist:
	cityParam = (city,)
	cursor.execute(queryPopulation, cityParam)
	count = 0
	for (population,) in cursor:
		#print(population)
		populationList.append(population)
		count += 1
		break
	if count == 0:
		print('city {0} have no population'.format(city))
	if count > 1:
		print('city {0} have {1} population'.format(city, count))

print('end of second result')
print(len(populationList))
cursor.close()




cnx.close()
