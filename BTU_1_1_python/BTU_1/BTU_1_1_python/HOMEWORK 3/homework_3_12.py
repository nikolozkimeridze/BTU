# შეიყვანეთ ნებისმიერი 2 რიცხვი. ციკლის გამოყენებით დაბეჭდეთ შეყვანილი რიცხვების საერთო გამყოფები. მაგ. 15-ის და 18-ის
# საერთო გამყოფებია: 1, 3
# first=int(input("Enter any number: "))
# second=int(input("Enter any number: "))
# if first < second:
    # for i in range(1 , first + 1):
        # if first % i == 0:
            # print(i, end = " ")
# elif second < first:            
    # for x in range(1 , second + 1):
        # if second % x == 0 :
            # print(x , end=" ")

#????????????????????????????????ამ გზას ვერ შევცვლი ასე უფრო მეკომფორტულება????????????????????????????????

#--------------სხვა გზა---------------------
first=int(input("Enter any number: "))
second=int(input("Enter any number: "))

if first > second:
    maxx=second
elif second > first:
    maxx=first
else:
    first==second and maxx==first and maxx==second

for i in range(1, maxx+1):
    if first % i == 0 and second % i ==0:
        print(i, end=" ")

    