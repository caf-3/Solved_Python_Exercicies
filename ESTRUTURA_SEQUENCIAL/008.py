# make a program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show your total salary in that month.
import os
try:
    #This will work in Linux Distros
    os.system("clear")
    #This will work on Windows
    #os.system('cls')
    m = input("Input the month: ")
    pH = float(input("How much do you earn per hour ($): "))
    nH = float(input("The number of hours worked in the mounth: "))
    #This will work in Linux Distros
    os.system("clear")
    #This will work on Windows
    #os.system('cls')
    print(f'Month: {m}\nIncome per hour: {pH}$\nHours worked: {nH}\nSalary: {pH*nH}$')
except Exception as E:
    print(f'An error occured: {E}')