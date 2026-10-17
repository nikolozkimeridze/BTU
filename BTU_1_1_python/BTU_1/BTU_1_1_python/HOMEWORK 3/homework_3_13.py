# 13. შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.
num1=int(input("Enter first number here: "))
num2=int(input("Enter second number here: "))

if num1>num2:
    maxx=num2
elif num1<num2:
    maxx=num1

for i in range( maxx+1, 1 , -1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break
