from urllib.request import urlopen
from xml.etree import ElementTree
import urllib

def getIDs(ip, queryword, ps=100):
    queryword = urllib.parse.quote(queryword)
    url = 'http://' + ip + '/mm/search.action?q=' + queryword + '&t=all&ps=%s&pid=1&f=W&s=L' % ps
    #print(url)
    response = urlopen(url)
    root = ElementTree.fromstring(response.readall())
    result_Node = root.find('result')
    size = result_Node.find('total').text
    goods = result_Node.find('list').findall('goods')
    lID = [good.getchildren()[0].text for good in goods]
    return size, lID


#print(getIDs('111.13.10.2', '小鸟'))
#print(len(getIDs('111.13.10.2', '鸟')))

#print(getIDs('111.13.10.2', '鸟', 10))

def interset(l1, l2, size):
    s1 = set(l1[:size])   
    s2 = set(l2[:size])
    #print(s1)
    #print(s2)
    #print(s1.intersection(s2))
    return len(s1.intersection(s2))

#print(interset([i for i in range(0, 100, 2)], [i for i in range(0, 100, 4)], 20))

def compare(r1, r2):
    if r1[0] == r2[0]:
        print('总结果数一致')
    else:
        print('总结果数不一致，分别为' + str(r1[0]) +', ' + str(r2[0]))

    count = min(len(r1[1]),len(r2[1]))   
    for i in range(count):
        if(r1[1][i] != r2[1][i]):
            print('顺序一致数量 %s' % i)
            break

    if count>=10:
        for i in range(10, count, 10):
            print('前' + str(i) + '里一致的数量为%s' % interset(r1[1], r2[1], 10))
    else:
        print('前' + str(count) + '里一致的数量为%s' % interset(r1[1], r2[1], count))
       
    
   

def mainProcess():
    ips = ('111.13.10.2', '111.13.10.41')
    querywordfile = 'queryword.txt'
    wordlist = [line.rstrip() for line in open(querywordfile)]    
    for word in wordlist:
        print(word)
        r1 = getIDs(ips[0], word)
        #print(r1)
        r2 = getIDs(ips[1], word)
        #print(r2)
        compare(r1, r2)
        print('')
            
mainProcess()
