# შექმენი ფუნქცია display_user(name, age), რომელიც სახელსა და ასაკს დაბეჭდავს და არაფერს
# დააბრუნებს. შეამოწმე, რომ ფუნქციის შედეგი None-ია.

def display_user(name, age):
    print(f" Name: {name},age: {age} ")
    #არ აქვს return და აბრუნებს None-ს

name=input("Enter your name here: ")
age=input("Enter your age here: ")
result=display_user(name, age)

print("Result is:", result)