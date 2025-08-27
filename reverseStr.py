#revesing a string using extended string slicing method
str="Hello Nithin"
print(str[::-1])

#without using slicing
s = "python"
rev = ""
for char in s:
    rev = char + rev
print("Reversed:", rev)
