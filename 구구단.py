#구구단
#단 반복용 for문 하나, 구구단 내부 반복용 하나

#구구단 내부 루프 먼저 구현
for dan in range(1,10):
    print("%d단" %dan)
    i=1
    while i<10:
        p=dan*i
        print("%d X %d= %d" %(dan, i, p))
        i+=1

        
    
    
    


