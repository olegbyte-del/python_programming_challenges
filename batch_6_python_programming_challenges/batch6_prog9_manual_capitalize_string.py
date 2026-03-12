# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

string = input("Please input a string: ")

upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijklmnopqrstuvwxyz")

result = ""

for i in range(len(string)):
    char = string[i]
    
    if i == 0:
        if char in lower:
            index = lower.index(char)
            result += upper[index]
        
        else:
            result += char
    
    else: 
        if char in upper:
            index = upper.index(char)
            result += lower[index]
            
        else:
            result += char
            
print(f"Result: {result}")