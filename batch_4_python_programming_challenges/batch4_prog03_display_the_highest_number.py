# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest 

highest_number = None

while True:
    try:
        number = int(input("Please input a number: "))
    
        if highest_number is None or number > highest_number:
            highest_number = number
            
    except ValueError:
        break

print(f"The highest number is: {highest_number}")