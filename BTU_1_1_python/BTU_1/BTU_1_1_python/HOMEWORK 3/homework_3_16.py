# შეიტანეთ რიცხვი. დაადგინეთ შეტანილი რიცხვი არის თუ არა მარტივი რიცხვი და გამოიტანეთ შესაბამისი შეტყობინება
# (გაითვლისწინეთ: მარტივია რიცხვი, რომელსაც აქვს მხოლოდ ორი გამყოფი: ერთი და თავისი თავი).
# 
# num=int(input("Enter any number here: "))
# if num == 1:
    # print("არც მარტივია და არც შედგენილი")
# elif num <= 0:
    # print("დადებითი რიცხვი შეიყვანე")
# 
# for i in range(2,num):
    # if num % i == 0:
        # print("არაა მარტივი რიცხვი")
        # break

# for x in range(2,num):
    # if num % x != 0:
        # print(" მარტივი რიცხვია")
        # break    
#ამ გზით არ გამომივიდა და რატომ ვერ მივხვდი სხვა გზა --------------

num=int(input("Enter any number here: "))
if num == 1:
    print("არც მარტივია და არც შედგენილი")
elif num <= 0:
    print("დადებითი რიცხვი შეიყვანე")
else:
    prime=False

for i in range(2,num):
    if num % i == 0:
        prime=False
        break
    else:
        prime=True
if prime == True:
    print("მარტივი რიცხვია")
else:
    print("არ არის მარტივი რიცხვი")