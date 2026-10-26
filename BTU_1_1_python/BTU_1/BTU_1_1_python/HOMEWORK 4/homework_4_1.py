# 1. შეიყვანეთ ათწილადი რიცხვი, დაამრგვალეთ მეათედის სიზუსტით (1 ციფრი ათწილად ნაწილში) და
# დაბეჭდეთ შედეგი. გამოიყენეთ round, ceil, floor, trunc ფუნქციები სათითაოდ და შეამოწმეთ შედეგი
# თითოეულის გამოყენებით.

number=float(input("Enter your number here: "))

print(round(number))

from math import ceil
print(ceil(number))

from math import floor
print(floor(number))

from math import trunc
print(trunc(number))        #trunc იგივე int-ია

