def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    
    return True

prime_n=[n for n in range(45,1224)if prime(n)]

print(prime_n)