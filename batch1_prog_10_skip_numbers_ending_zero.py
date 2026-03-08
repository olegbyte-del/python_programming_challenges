# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

print("="*50, "Program 1".center(50), "="*50, sep="\n")
print("prints all the numbers from 0 to 100", 
        "except numbers that ends in zero.", "="*50, sep='\n')

numbers = []

for i in range(101):
    if i % 10 != 0:
        numbers.append(i)
        print([i], end=' ')