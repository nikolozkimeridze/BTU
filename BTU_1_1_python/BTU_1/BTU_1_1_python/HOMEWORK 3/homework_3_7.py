# 7. შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო
# არითმეტიკული.
total=0
for i in range(10):
    num=float(input("Enter the number: "))
    total += num
average= total / 10
print(average)