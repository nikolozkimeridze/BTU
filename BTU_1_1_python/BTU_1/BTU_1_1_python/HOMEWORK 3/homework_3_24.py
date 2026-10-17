# შეიყვანეთ ნებისმიერი რიცხვი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი. (მითითება:
# პალინდრომია რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება).
# მაგ. 12521 არის პალინდრომი

number=input("Enter anu number here: ")
new_number=""
for i in number:
    new_number= i + new_number
if int(new_number)==int(number):
    print("პალინდრომი რიცხვია")
else:
    print("არ არის პალინდრომი რიცხვი")