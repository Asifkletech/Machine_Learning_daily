#armstrong example=371

num=371
temp=num
length=len(str(num))
sum=0
while num>0:
    rem=num%10
    sum+=pow(rem,length)
    num=num//10
    
if sum==temp:
    print("armstrong number")

else:
    print("not a armstrong number")