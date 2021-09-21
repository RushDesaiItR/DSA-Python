def palindrome(str):
    return str == str[::-1]
s="sdddsff"
if(palindrome(s)):
    print("Palindrome String")
else:
    print("Not A Palindrome String")    