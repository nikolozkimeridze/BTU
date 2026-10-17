# შეიყვანეთ ნებისმიერი რიცხვი. დაბეჭდეთ შეტანილი რიცხვი შებრუნებული სახით. (მითითება: მაგ. თუ შეიტანთ 1254-ს,
# დაბეჭდოს 4521). არ გააკეთოთ სტრიქონის ტიპის მონაცემისთვის.

new_number=""
number=input("Enter any number: ")
for i in number:
    new_number = i + new_number
print(new_number)
