# შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ. (len ფუნქციის გარეშე)
num=int(input("enter the number here: "))
xarisxi=1
if num <10:
    print(1)
elif num==10:
    print(2)
while num > 10**xarisxi:
    xarisxi+=1
print(xarisxi)
    
