# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

string = input("please input a string: ")

upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijklmnopqrstuvwxyz")

result = ''
for char in string:
    if char in upper:
        index = upper.index(char)
        
        result += lower[index]
    
    elif char in lower:
        index = lower.index(char)
        
        result += upper[index]
        
print(f"Result: {result}")