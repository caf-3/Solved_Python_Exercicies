# Make a Program that asks for the 4 bimonthly notes and shows the average.
try:
    print("#### Please : Input your 4 bimonthly notes")
    n1 = float(input("Note 1: "))
    n2 = float(input("Note 2: "))
    n3 = float(input("Note 3: "))
    n4 = float(input("Note 4: "))
    average = (n1 + n2 + n3 + n4) / 4
    print(f'Average : {average}')
except Exception as E:
    print("Please, input valid numbers")