inFp=None
inStr=""

inFp=open("C:\\Users\\User\\Documents\\학교 자료\\파이썬 프로그래밍\\Pythontest\\data1.txt","r",encoding='UTF8')

line=1

while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print("%d: %s" %(line, inStr), end="")
    line+=1

inFp.close()