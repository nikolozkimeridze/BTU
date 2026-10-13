year=int(input("Enter the any year you want and i will tell if it is a leap year: "))

if (year % 4 == 0 or year % 100 == 0) and (year % 400 != 0):
    print("it is a leap year")
else:
    print("it is not a leap year")