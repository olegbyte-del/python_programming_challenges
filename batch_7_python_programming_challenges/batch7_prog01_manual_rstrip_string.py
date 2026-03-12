# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

string = input("Please input a string with additional spaces: ")

space_list = []

for i in string:
    if string[i] == " ":
        space_list.append(i)
        
    