# შექმენი ფუნქცია factorial(number), რომელიც არაუარყოფითი მთელი რიცხვის ფაქტორიალს
# დააბრუნებს. მაგალითად, factorial(5) აბრუნებს 120-ს. არ გამოიყენოთ math-ის ფაქტორიალის ფუნქცია.

def factorial(number):
    res=1
    if number == 0:
        print("0")
    elif number < 0:
        print(f"{number}-ს არ აქვს ფაქტორიალი")
    else:
        for i in range(number):
            res += (res*i)
        print(res , f"ეს არის {number}-ის ფაქტორიალი")
   
number=int(input('Enter your number here: '))
factorial(number)