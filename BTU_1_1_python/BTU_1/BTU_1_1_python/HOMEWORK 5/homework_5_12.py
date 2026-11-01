# 12. შექმენი ფუნქცია introduce(name, country='Georgia'), რომელიც დაბეჭდავს ადამიანის სახელსა და
# ქვეყანას.

def introduce(name, country='Georgia'):
    print(name , country , end= " ")

# თავიდან წინა სავარჯიშოებში მეგონა რომ name თუ იყო ფუნქციაში ცვლადი რომელსაც დაბლა ვწერდით სხვა სახელით უნდა ყოფილიყო
name = str(input("Enter your name here: "))
country = str(input("Enter your country here: "))

introduce(name, country)
