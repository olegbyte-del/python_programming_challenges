# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

list_number = []
for i in range(10):
    try:
        number = int(input("Please input a number: "))
        list_number.append(number)
        
        result = list_number[0] - sum(list_number[1:])
    
    except ValueError:
        print("Please input a valid input!")
        
print(result)