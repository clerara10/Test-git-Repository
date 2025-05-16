inFp, outFp=None, None
inStr=""

inFileName = input("복사할 원본 파일명을 입력하세요: ")
outFileName = input("복사된 내용을 저장할 파일명을 입력하세요: ")

inFp=open("C:/Windows/win.ini", "r")
outFp=open("C:/Temp/data1.txt", "w")

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("----파일이 정상적으로 복사되었음-----")