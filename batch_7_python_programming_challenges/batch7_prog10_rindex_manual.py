# Create a program that asks the user to input a string and a substring, then prints the last occurrence index of the substring in the string, implementing the functionality of rindex() manually without using the built-in function.

print("="*50, "Program 6".center(50), "="*50, sep="\n")
print("Create a program that asks the user to input a string and a substring", 
        "then prints the last occurrence index of the substring in the string",
        "implementing the functionality of rindex() manually without using the built-in function.", "="*50, sep='\n')

main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to find: ")

last_index = -1

for i in range(len(main_string)):
    if main_string[i:i+len(sub_string)] == sub_string:
        last_index = i

    if last_index != -1:
        print("The last occurence is at index: ", last_index)
    else:
        print("Substring not found!")
    