# შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით. იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი და დაბეჭდეთ. თუ კენტი რიცხვი არ
# შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.

max_odd=0
find_odd=False

for i in range(10):
    prompt="Enter " + str(i+1)  + " number: "
    number=int(input(prompt))

    if number % 2 == 1:
        if number > max_odd or find_odd == False:
            max_odd=number
            find_odd=True
if find_odd == True:
    print(max_odd)
  