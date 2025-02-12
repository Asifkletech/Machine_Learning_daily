#A Number that is equal to the sum of the factorial of it's individual digits is known as Strong Number.
#Example=145=  1!+4!+5!=  1+24+120(145)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        
    return fact

def strong(num):
    sum_of_fact=0
    original_num=num
    while num>0:
        
        
        rem=num%10
        sum_of_fact+=factorial(rem)
        num=num//10
    
    return sum_of_fact==original_num
num=145
if strong(num):
    print("strong number")
    
else:
    print("not a strong number")
    

