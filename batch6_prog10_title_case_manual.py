# Create a program that asks the user to input a string and prints the input in title case manually, capitalizing the first letter of each word without using the built-in title() function.

print("="*50, "Program 6".center(50), "="*50, sep="\n")
print("program that asks the user to input a string and prints the input in", 
        "title case manually capitalizing the first letter of each word without",
        "husing the built-in title() function..", "="*50, sep='\n')

user_input = input("Enter a string: ")

word_list = user_input.split()

formatted_words = []

for word in word_list:
    format = word[0].upper() + word[1:].lower() 
    formatted_words.append(format)