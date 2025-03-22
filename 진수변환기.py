#값 입력 로직
#진수로 입력 받음-> 해당 진수로 값 입력 받음->10진수로 변환
print("입력 진수 결정(16/10/8/2): ")
a=input()


if a==str(16):
    print("값 입력: ")
    b=input()
    int_value=int(b,16) #16진수로 해석해서 10진수로 변환함
    value_hex=hex(int_value)
    value_oct=oct(int_value)
    value_bin=bin(int_value)

    print("16진수는 ==> %s\n10진수는 ==> %s\n8진수는 ==>  %s\n2진수는 ==>  %s" %(value_hex,int_value ,value_oct ,value_bin))
    

if a==str(10):
    print("값 입력: ")
    b=input()
    int_value=int(b) 
    value_hex=hex(int_value)
    value_oct=oct(int_value)
    value_bin=bin(int_value)

    print("16진수는 ==> %s\n10진수는 ==> %s\n8진수는 ==>  %s\n2진수는 ==>  %s" %(value_hex,int_value ,value_oct ,value_bin))

if a==str(8):
    print("값 입력: ")
    b=input()
    int_value=int(b,8) #8진수로 해석해서 10진수로 변환함
    value_hex=hex(int_value)
    value_oct=oct(int_value)
    value_bin=bin(int_value)

    print("16진수는 ==> %s\n10진수는 ==> %s\n8진수는 ==>  %s\n2진수는 ==>  %s" %(value_hex,int_value ,value_oct ,value_bin))

if a==str(2):
    print("값 입력: ")
    b=input()
    int_value=int(b,2) #16진수로 해석해서 10진수로 변환함
    value_hex=hex(int_value)
    value_oct=oct(int_value)
    value_bin=bin(int_value)

    print("16진수는 ==> %s\n10진수는 ==> %s\n8진수는 ==>  %s\n2진수는 ==>  %s" %(value_hex,int_value ,value_oct ,value_bin))




    







