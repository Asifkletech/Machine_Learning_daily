num=1222
temp=num
rev=0

while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
    
if rev==temp:
    print("number is a palindrome")
    
else:
    print("number is not a palindrome")