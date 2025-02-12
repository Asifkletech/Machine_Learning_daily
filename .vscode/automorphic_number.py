num=76

square=pow(num,2)
m=pow(10,len(str(num)))

if square%m==num:   
    print(num,"is a automorphic ")
    
else:
    print(num," is not automorphic")
    
    
