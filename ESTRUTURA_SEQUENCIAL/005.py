# Make a Program that converts meters to centimeters.
try:
    m = float(input("Input meters (m) :"))
    c = m * 100
    print(f'{m}(m) -> {c}(cm)')
except Exception as E:
    print('Please input a valid number')