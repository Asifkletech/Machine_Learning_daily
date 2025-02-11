def prime_factor(n):
    
    i=2
    while i*i<=n:
        while n%i==0:
            print(i,end=" ")
            n=n//i
            
        i=i+1
        if n>1:
            print(n)
            
n=10
#num = int(input("Enter a number: "))
#print("Prime factors:", end=" ")
        
prime_factor(n)      