#დავალება 1: ხელფასისა და ბონუსების კალკულატორი
#პირობა: დაწერეთ პროგრამა, რომელიც ითვლის თანამშრომლის წმინდა ხელფასსა და წუთობრივ ანაზღაურებას.
sal_hours=float(input("Enter the the payment you are getting in an hour: "))
work_days=float(input("Enter the amount of days that you are working during the month: "))
salary=sal_hours*work_days
salary_with_taxes=salary- 0.3*(salary)
#წუთები და წამები ხელფასი TAX NO
per_min=salary/60
per_sec=per_min/60
#წუთები და წამები ხელფასი TAX !!
per_min_tax=salary_with_taxes/60
per_sec_tax=per_min_tax/60

  
question_1=input("Enter what you want to know  - with taxes or without taxes")
if question_1=="with taxes":
    print(per_min_tax)
    print(per_sec_tax)
elif question_1=="without taxes":
    print(per_min)
    print(per_sec)
else:
    print(per_min , "WITH TAXES")
    print(per_sec ,  "WITH TAXES")
    print(per_min_tax,  "WITHOUT TAXES")
    print(per_sec_tax,  "WITHOUT TAXES")
