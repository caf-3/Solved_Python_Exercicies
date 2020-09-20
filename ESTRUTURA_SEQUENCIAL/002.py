# Make a Program that asks for a number and then displays the message The number entered was [number].try:
    number = float(input('Write a number :'))
    print(f'The number written was: {number}')
except Exception as Err:
    print("Not a number input was given" )
