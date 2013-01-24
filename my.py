#path = r'G:\Intellis\3.2.2\index\ePaperIndex\AuxData\FullText.txt'
path = r'G:\Intellis\3.2.3\bin\content3.txt'
destpath = r'G:\content3.txt'
count = 0
total = 0
contentfile = open(path)
dest = open(destpath, 'w')
while True:
    try:
        total += 1
        line = contentfile.readline()
        l = line.split()
        if len(l[0]) > 10:      
            count+=1
            dest.write(l[0] + '\n')
            if count % 10000 == 0:
                print(count, total)
    except:        
        print('error, total = ' + str(total) + ' count = ' + str(count))
        break

contentfile.close()
dest.close()
print('end total = ' + str(total) + ' count = ' + str(count))
                
    

