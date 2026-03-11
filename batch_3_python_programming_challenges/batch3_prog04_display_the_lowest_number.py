# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number


lowest_number = None

for i in range(100):
    try:
        user_number = int(input("Please input a number: "))
        number = int(number)

        if lowest_number is None or number < lowest_number:
            lowest_number = number
        
    except ValueError:
        print("Invalid input!")
        break
    
print(f"the lowest number entered was: {lowest_number}")