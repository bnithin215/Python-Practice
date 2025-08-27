arr=[20,34,24,36,1,4]
largest=arr[0]
smallest=arr[0]

for num in arr:
    if num > largest:
        largest=num
    if num < smallest:
        smallest=num 
print("smallest:",smallest) 
print("largest:",largest)          