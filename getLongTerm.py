#path = r'G:\Intellis\3.2.2\index\ePaperIndex\AuxData\FullText.txt'
path = r'G:\Intellis\3.2.3\bin\textik.txt'
destpath = r'G:\textik.txt'


def getLongTerm(source, dest):
    count = 0
    total = 0
    contentfile = open(path, mode='r', encoding='gb18030')
    dest = open(destpath, 'w')
    while True:
        try:
            total += 1
            line = contentfile.readline()
            l = line.split()
            s = l[0]
            print(l[0])
            if len(l[0]) > 20:
                count += 1
                dest.write(l[0] + '\n')
                if count % 10000 == 0:
                    print(count, total)
        except:
            by = s.encode('gb18030')
            utfStr = by.decode('utf-8')
            print('error, total = ' + str(total) + ' count = ' + str(count))
            print('error line:' + utfStr)
            #break

    contentfile.close()
    dest.close()
    print('end total = ' + str(total) + ' count = ' + str(count))

if __name__ == '__main__':
    getLongTerm(path, destpath)
