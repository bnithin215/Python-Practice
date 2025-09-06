arr=[1,2,33,44,55,23,54,67,89,91,98,99]
def secondLargest(arr):
    unique=list(set(arr))
    if len(unique) <2:
        return none 
    unique.sort()
    return unique[-2]
print(secondLargest(arr))        