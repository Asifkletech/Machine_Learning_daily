n=14
temp=n
length=len(str(n))
sum=0

while n>0:
  rem=n%10
  sum+=pow(rem,length)
  n=n//10
  
if sum==temp:
  print("It is a Armstrong")
  
else:
  print("the number is not a Armstrong")
  
