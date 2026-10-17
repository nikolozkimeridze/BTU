# # შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა ჯამი და დაბეჭდეთ.
# num=int(input("Enter the number here: "))
# sum=0
# for i in range(num):    #!!!!!!!!!!!!!!!!!აქ არ მახსოვდა რომ ასე ტქსტის განხილვისას input-ში int არ უნდა ყოფილიყო  და AI დავიხმარე ამ კოდზე ვკითხე რა პრობლემა იყო!!!!!!!!!!!
#     sum+=i
# print(sum)


num=input("Enter the number here: ")
sum=0
for i in num:
    sum+=int(i)
print(sum)
