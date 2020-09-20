# Make a Program that asks for two numbers and prints the sum.
try:
    print("#### Enter two numbers to get the sum of them : ")
    num1 = float(input("Number 1: "))
    num2 = float(input('Nubmer 2: '))
    print(f'{num1} + {num2} = {num1 + num2}')
except Exception as Err:
    print("Not a number value was given")