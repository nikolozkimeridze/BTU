name=input("Enter the bank you want to withdraw money: TBC/BOG/LIBERTY/OTHER")
#days=float(input("Enter the days you works: "))
#hours=float(input("Enter the hours you work: "))
#amount=input("Enter the amount you want to withdraw: ")
#savings=float(input("Enter your savings for a whole life: "))
#question_about_other_savings=float(input("Do you have any other saveings: YES/NO: "))
#amount_of_other_savings=float(input("Enter your other savings: "))
other_savings=0
if name=="TBC":
    days=float(input("Enter the days you works: "))
    hours=float(input("Enter the hours you work: "))
    salary=days*hours
    print(salary , "is your income")
    savings=float(input("Enter your savings for a whole life: "))
    question_about_other_savings=float(input("Do you have any other saveings: YES/NO: "))

    if question_about_other_saving == "YES":
        amount_of_other_savings=float(input("Enter your other savings: "))
        other_saving+=amount_of_other_savings
        print("Thats great you can withdraw", salary+savings+other_savings)
    else:
        print("thats okay because of this you can only withdraw : " , salary+savings)



    amount=input("Enter the amount you want to withdraw: ")
    # if amount > salary:
elif name==BOG:
    days=float(input("Enter the days you works: "))
    hours=float(input("Enter the hours you work: "))
    print(days*hours , "is your income")
    savings=float(input("Enter your savings for a whole life: "))
    question_about_other_savings=float(input("Do you have any other saveings: YES/NO: "))

elif name==LIBERTY:
    days=float(input("Enter the days you works: "))
    hours=float(input("Enter the hours you work: "))
    print(days*hours , "is your income")
    savings=float(input("Enter your savings for a whole life: "))
    question_about_other_savings=float(input("Do you have any other saveings: YES/NO: "))
else:
    print("we do not accept other bank cards here")