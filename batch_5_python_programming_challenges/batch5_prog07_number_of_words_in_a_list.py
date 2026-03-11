# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

statement = input("Please input a statement: ")

word_list = statement.split()
word_count = len(word_list)
print(f"The number of words in the input is: {word_count}")



