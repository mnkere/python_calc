# This is a simple calculator program that performs basic arithmetic operations.
# Ask for two numbers
No_1 = float(input("Enter first number: "))
No_2 = float(input("Enter second number: "))

# Ask for operation choice
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
calcl = input("Enter operator (+, -, *, /): ")

# Perform operation based on input
if calcl == "+":
    result = No_1 + No_2
    print(f"\nResult: {No_1} + {No_2} = {result}")
elif calcl == "-":
    result = No_1 - No_2
    print(f"\nResult: {No_1} - {No_2} = {result}")
elif calcl == "*":
    result = No_1 * No_2
    print(f"\nResult: {No_1} * {No_2} = {result}")
elif calcl == "/":
    if No_2 != 0:
        result = No_1 / No_2
        print(f"\nResult: {No_1} / {No_2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")
else:
    print("\nInvalid operator selected!")
# End of the calculator program