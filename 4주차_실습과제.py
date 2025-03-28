print("1. 입력한 수식 계산 2. 두 수 사이의 합계")
x=int(input())



if x == 1:
    print("***수식을 입력하시오: ")
    y=input("")
    value=eval(y)
    print("%s 결과는 %f 입니다." %(y, value))


else:
    print("첫 번째 숫자를 입력하세요: ")
    add1=int(input())
    print("두 번째 숫자를 입력하세요: ")
    add2=int(input())

    #add1 과 add2의 크기를 비교해서 크기순서로 다시 정리
    #add1의 크기가 add2보다 크게

    temp=0
    if(add1<add2):
        add1,add2=add2,add1
    num=add2
    result=0
    while add2<=add1:
        result+=add2
        add2+=1
    print("%d+...+%d는 %d입니다" %(num, add1, result))





  





    







