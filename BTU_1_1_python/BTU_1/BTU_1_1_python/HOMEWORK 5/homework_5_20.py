# შექმენი ფუნქცია calculate(a, b, operation='+'), რომელიც შეკრებას, გამოკლებას ან გამრავლებას
# შეასრულებს operation პარამეტრის მიხედვით. არასწორი ოპერაციისთვის დააბრუნე შესაბამისი
# შეტყობინება.


def calculate(a , b , operation = '+'):
    # if operation == " ":
    #     return a+b
    if operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    elif operation == "//":
        return a//b
    elif operation == "%":
        return a%b
    else:
        return a+b
a=int(input("Enter any number: "))
b=int(input("Enter any number: "))
operation=input("Enter operation: ")
print(calculate(a,b,operation))