def reverseString(str):
    s = ""
    for i in str:
        s=i+s
    return s
hereString = "rushikesh"
print("Before Revserse A String ", end=" ")
print(hereString)
print("After Reverse String ", reverseString(hereString))        