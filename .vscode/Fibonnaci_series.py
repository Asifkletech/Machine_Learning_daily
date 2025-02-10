n=10
n1,n2=0,1

for i in range(n-2):
    n3=n2+n1
    n1=n2
    n2=n3
    
    print(n3)