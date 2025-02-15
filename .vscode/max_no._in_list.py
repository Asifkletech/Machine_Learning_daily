lst=[1,3,45,67,899,34,56,78]

maxNum=lst[0]

for num in lst:
    if maxNum<num:
        maxNum=num
        
print(maxNum)