# Make a program that calculates the area of ​​a square, then show the double of this area to the user.
try:
    side = float(input("Input the square side : "))
    print(f'The double of the square area is: {side**3}')
except Exception as E:
    print("Please, input a valid number.")