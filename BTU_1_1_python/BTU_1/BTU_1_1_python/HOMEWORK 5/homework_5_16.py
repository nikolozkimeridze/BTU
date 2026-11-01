# შექმენი ფუნქცია find_max(a, b, c), რომელიც სამ რიცხვს შორის უდიდესს დააბრუნებს max()-ის
# გამოყენების გარეშე.
def find_max(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
a=float(input("Enter first number here: "))
b=float(input("Enter first number here: "))
c=float(input("Enter first number here: "))

find_max(a,b,c)