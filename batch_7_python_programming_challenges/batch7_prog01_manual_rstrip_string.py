# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

string = input("Please input a string with additional spaces: ")

space_list = -1

for i in range(len(string)):
    if string[i] != " ":
        space_list = i
        
result = string[:space_list + 1]
print(f"Result: {result}")