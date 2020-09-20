# Make a Program that asks for the radius of a circle, calculate and show its area
try:
    r = float(input('Enter the radius of the circle :'))
    area = 3.14 * r
    print(f'The area of the circle is {area}')
except Exception as E:
    print("Please, input a valid number")
