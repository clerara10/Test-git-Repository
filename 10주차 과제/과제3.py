outFp=None
outStr=""

fileName=input("저장할 파일명을 입력하세요: ")

outFp=open("C:\\Users\\User\\Documents\\학교 자료\\파이썬 프로그래밍\\Pythontest\\data1.txt", "w")

while True:
    outStr=input("내용 입력: ")
    if outStr!="":
        outFp.writelines(outStr+"\n")

    else:
        break

outFp.close()
print("----정상적으로 파일에 씀----")