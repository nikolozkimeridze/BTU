# 11. შეიყვანეთ რიცხვი კლავიატურიდან. პროგრამამ უნდა დაბეჭდოს შეყვანილი რიცხვის ყველა გამყოფი. (მაგ. 18-ის გამოყოფებია: 1,
# 2, 3, 6, 9, 18)
x=int(input("Enter the any number you want and after this we will show all number that it can be divided: "))
for i in range(1, x+1):
    if x % i == 0:
        print(i , end=" ")
