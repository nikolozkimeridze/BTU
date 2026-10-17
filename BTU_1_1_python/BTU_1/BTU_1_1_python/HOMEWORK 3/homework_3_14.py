# შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი. #აქ შემეშალა და გამყოფზე დავწერე ეს მაინც 1 იქნებოდა ყველა შემთხვევაში მარა მაინც დავტოვე
# num1=int(input("Enter the first number here: "))
# num2=int(input("Enter the second number here: "))

# if num1>num2:
    # maxx=num2
# elif num1<num2:
    # maxx=num1
# for i in range(1, maxx+1):
    # if num1 % i == 0 and num2 % i == 0:
        # print(i)
        # break


# შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.
num1=int(input("Enter first number here: "))
num2=int(input("Enter second number here: "))
if num1 > num2:
    maxx=num1
elif num2 >num1:
    maxx=num2
maxxx=maxx  #მუდმივი ცვლადი----- ანუ მაქსიმალური  maxxx

while True:
    if maxx % num1==0  and maxx % num2 == 0:
        break
    maxx += maxxx #მოზრავი ცვლადი--- ემატება უდიდესი რიცხვი სანამ ორივე უნაშთოდ არ გაიყოფა
print(maxx)