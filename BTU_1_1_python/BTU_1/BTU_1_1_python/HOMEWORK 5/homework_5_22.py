# შეასრულეთ მე-18 დავალება რეკურსიის გამოყენებით. რეკურსიულია ფუნქცია რომელიც თავის თავს
# იძახებს.

# შექმენი ფუნქცია factorial(number), რომელიც არაუარყოფითი მთელი რიცხვის ფაქტორიალს
# დააბრუნებს. მაგალითად, factorial(5) აბრუნებს 120-ს. არ გამოიყენოთ math-ის ფაქტორიალის ფუნქცია.

def factorial(number):
    # if number==0:
    #     return 0
    if number==1 or number==0:
        return 1
    return number * factorial(number-1)

number=int(input("Enter number here: "))
print(factorial(number))