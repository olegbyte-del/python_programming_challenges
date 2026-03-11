# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
list_numbers = []
for i in range(10):
    try:
        number = int(input("Please input a number: "))
        list_numbers.append(number)
    except ValueError:
        print("Invalid Input. Please enter an integer number.")
        
total_sum = sum(list_numbers)

print(f"The sum of all numbers is: {total_sum}")
    
    
        
