num=23
p=num
rem=0
while num>0:
    rem+=num%10
    
    num=num//10
   
if p%rem==0:
    print(p,"Harshad Number")
    
else:
    print(p,"not a Harshad Number")