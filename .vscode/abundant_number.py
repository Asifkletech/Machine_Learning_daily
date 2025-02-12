n=12
sum=1
for i in range(2,n):
    if n%i==0:
        sum=sum+i
        
if sum>n:
    print("abundant")
else:
    print("not a abundant")
    