string="madam"
def checkPalindrome(string):
    # remove spaces if you want to ignore them
    string = string.replace(" ", "")
    
    start = 0
    end = len(string) - 1
    
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True
print(checkPalindrome(string));