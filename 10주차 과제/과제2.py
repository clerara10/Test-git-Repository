# inFp=None
# inList=""

# inFp=open("C:\\Users\\User\\Documents\\학교 자료\\파이썬 프로그래밍\\Pythontest\\data1.txt","r",encoding='UTF8')

# inList=inFp.readlines()
# print(inList)

# inFp.close()

inFp=None
inList=""

inFp=open("C:\\Users\\User\\Documents\\학교 자료\\파이썬 프로그래밍\\Pythontest\\data1.txt","r",encoding='UTF8')
inList=inFp.readlines()

i=1
for inStr in inList:
    print("%d: %s" % (i, inStr), end="")
    i+=1

inFp.close()