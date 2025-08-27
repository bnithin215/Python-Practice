arr=[1,2,3,4,5,5,2,4]
result=[]
for num in arr:
    if not num in result:
        result.append(num)
print(result)        