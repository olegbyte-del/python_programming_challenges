# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average

number_list = []

while True:
    try:
        number = int(input("Please input a number: "))
        number_list.append(number)
    except ValueError:
        break
    
average = sum(number_list) / len(number_list)
print(f"The average is: {average}")