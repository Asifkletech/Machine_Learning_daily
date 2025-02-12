def is_square(n):
    if n<0:
        return False
    
    i=0
    while i*i<=n:
        if i*i==n:
            return True
        
        i=i+1
    return False

num=10
if is_square(num):
    print("perfect square")
    
else:
    print("not a perfect square")