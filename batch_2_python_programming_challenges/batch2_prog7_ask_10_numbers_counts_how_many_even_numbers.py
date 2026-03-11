# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

list_number = []
even_counter = 0
for i in range(10):
    try:
        number = int(input("Please input a number: "))
        
        if number % 2 == 0:
            even_counter += 1
    
    except ValueError:
        print("Please input a valid input!")
        
print(f"There are {even_counter} even numbers")