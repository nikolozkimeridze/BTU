# შექმენი ფუნქცია check_number(number), რომელიც დაბეჭდავს, რიცხვი ლუწია თუ კენტი.
def check_number(number):
    if number % 2 == 0:
        print(f"{number} , ლუწია")
    elif number % 2 == 1:
        print(f"{number} , კენტია")
    else:
        print(f"{number} , 0-ია")
number1=int(input("Enter the number here: "))
check_number(number1)