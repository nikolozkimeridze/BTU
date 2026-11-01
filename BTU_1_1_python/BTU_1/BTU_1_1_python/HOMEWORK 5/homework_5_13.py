# შექმენი ფუნქცია power(number, exponent=2), რომელიც რიცხვს მოცემულ ხარისხში აიყვანს. თუ
# ხარისხი მითითებული არ არის, რიცხვი კვადრატში აიყვანე.
def power(number , exponent = 2):
    print(number ** float(exponent))
number=float(input("Enter the number here: "))
exponent=input("Enter the exponent here: ")

if exponent == "":
    power(number , 2)
else:
    power(number , exponent)
