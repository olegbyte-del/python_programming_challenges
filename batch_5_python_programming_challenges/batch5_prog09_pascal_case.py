# Create a program that asks the user to input their fullname in incorrect casing and prints the input in PascalCase, where the first letter of each word is capitalized and all other letters are lowercase

print("="*50, "Program 5".center(50), "="*50, sep="\n")
print("program that asks the user to input their fullname ", 
        "in incorrect casing and prints the input in PascalCase,",
        "here the first letter of each word is capitalized and all other letters are lowercase.", "="*50, sep='\n')

user_name = input("Please enter your fullname: ")

pascal_name_version = user_name.title()

print(pascal_name_version.replace(" ", ""))

