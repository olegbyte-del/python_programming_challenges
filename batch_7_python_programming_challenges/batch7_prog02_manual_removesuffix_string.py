# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

text_file = input("Please input the text file including the file type: ")
identify_suffix = input("Please identify the type of file you want to remove: ").lower()

remove_suffix = len(identify_suffix)

if text_file[-remove_suffix:] == identify_suffix:
    format_version = text_file[:-remove_suffix]
else:
    format_version = text_file
    
print(f"Result: {format_version}")