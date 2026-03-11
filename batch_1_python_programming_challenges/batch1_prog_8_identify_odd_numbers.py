# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

list_numbers = []
count_odd_numbers = 0
for i in range(10):
    try:
        number = int(input("Please input a number: "))
        list_numbers.append(number)
        
        if i % 2 == 0:
            count_odd_numbers += 1
            
    except ValueError:
        print("Invalid Input. Please enter an integer number.")

print(f"There are {count_odd_numbers} odd numbers")

