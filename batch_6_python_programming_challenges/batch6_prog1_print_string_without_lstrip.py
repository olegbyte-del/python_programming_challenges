# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

word = input("Please input a word: ")

number_of_spaces = 0
while number_of_spaces < len(word) and word[number_of_spaces] == " ":
    number_of_spaces +=1
    
print(word[number_of_spaces:])