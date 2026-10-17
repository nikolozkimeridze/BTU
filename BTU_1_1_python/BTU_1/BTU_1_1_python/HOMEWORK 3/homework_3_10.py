# 10. შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ.
# მაგ. 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5

x=int(input("Enter the number: "))
total=1
for i in range(1 , x+1):
    total *= i
print(total)

