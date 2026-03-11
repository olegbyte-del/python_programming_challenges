# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

list_of_characters = []

word = input("Enter text: ")

upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijklmnopqrstuvwxyz")

lowercase = ""

for char in word:
    if char in upper:
        index = upper.index(char)
        lowercase += lower[index]
    else:
        lowercase += char
        
print("Lowercase:", lowercase)
        
