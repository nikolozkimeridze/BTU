# 1 )რა იქნება გამოსახულებების შედეგი? გამოიყენეთ კონსოლი

# --------------------------------------    --------------------------------------    --------------------------------------   
# 
# 
#  
# a) True and false
# b) True and False
# c) False or not True
# d) not True or not False
# e) not (True and False)
# f) True and not False and not True
# g) not 0
# h) not 1
# i) not 2
# j) False or 52 > 5
# k) 12 != 12.0
# l) 24 <= 25.6
# m) 116 - 5 == 111
# n) 4 < 6 < 23
# o) 7 < 3 < 4
# p) 1 < 2 < 3 < 4 == 5 < 6
# q) 1 < 2 < 3 < 4 != 5 < 6
# r) 1 < 2 < 3 < 4 < 4 < 5
# s) 1 < 2 < 3 < 4 >= 4 < 5
# t) True or False and False
# u) (True or False) and False


 #print(True and false) #--------------------------------------                    
print(True and False)   # False                
print(False or not True) #False
print(not True or not False) #True
print(not (True and False)) #True
print(True and not False and not True) #False
print(not 0) #False
print(not 1) #True
print(not 2) #False
print(False or 52 > 5) #True
print(12 != 12.0) #False
print(24 <= 25.6) #True
print(116 - 5 == 111) #True
print(4 < 6 < 23)# True
print(7 < 3 < 4) #False
print(1 < 2 < 3 < 4 == 5 < 6) #False
print(1 < 2 < 3 < 4 != 5 < 6) #True
print(1 < 2 < 3 < 4 < 4 < 5) #False
print( 1 < 2 < 3 < 4 >= 4 < 5) #True
print(True or False and False) #True რადგან ჯერ and ოპერატორს პრიორიტეტი აქ
print((True or False) and False) #False


# --------------------------------------    --------------------------------------    --------------------------------------    


# 2) დაწერეთ პროგრამა, რომელიც შეამოწმებს მომხმარებლის მიერ შეყვანილ რიცხვს და
# თუ დადებითია, დაბეჭდავს "შეყვანილი რიცხვი დადებითია" .

num=float(input("Enter your number and we will check if your number is bigger than 0: " ))

if num > 0:
    print("შეყვანილი რიცხვი დადებითია")
elif num <0:
    print("შენი რიცხვი უარყოფითია")
elif num==0:
    print("თქვენი შეყვანილი რიხვი არც დადებითია და არც უარყოფითი")
else:
    print("სცადეთ თავიდან და შეიყვანეთ რიცხვი")


# --------------------------------------    --------------------------------------    --------------------------------------    



#3)დაწერეთ პროგრამა, რომელიც მომხმარებელს შეაყვანინებს რიცხვს. პროგრამამ უნდა
# შეამოწმოს არის თუ არა რიცხვი 10-ის ჯერადი და დაწეროს "შეყვანილი რიცხვი
# ბოლოვდება 0-ით" ან "შეყვანილი რიცხვი არ ბოლოვდება 0-ით" შესაბამისად. (10-ის
# ჯერადი რიცხვი ნიშნავს რომ 10 ზე გაყოფისას ნაშთი არის 0)
num_multiple_check_10=float(input("Enter the number: "))
if num_multiple_check_10 % 10 == 0:
    print("შეყვანილი რიცხვი ბოლოვდება 0-ით")
else:
    print("შეყვანილი რიცხვი არ ბოლოვდება 0-ით")



# --------------------------------------    --------------------------------------    --------------------------------------    


# 4) დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება 2 რიცხვს. პროგრამამ
# უნდა შეამოწმოს, თუ ორივე რიცხვი მეტია 10-ზე, მაშინ დაბეჭდოს მათი ჯამი, ხოლო
# წინააღმდეგ შემთხვევაში დაბეჭდოს მათი ნამრავლი.
num_1=float(input("Enter the first number here: "))
num_2=float(input("Enter the second number here: "))
if num_1 > 10 and num_2 > 10:
    print(num_1+num_2)
else:
    print(num_1*num_2)


# --------------------------------------    --------------------------------------    --------------------------------------    


# 5) დაწერეთ პროგრამა, რომელიც შეამოწმებს მომხმარებლის მიერ შეყვანილ რიცხვს და
# თუ დადებითია, დაბეჭდავს "შეყვანილი რიცხვი დადებითია", თუ უარყოფითია
# დაბეჭდავს "შეყვანილი რიცხვი უარყოფითია", თუ არადა დაბეჭდავს "შეყვანილი
# რიცხვი არის 0".


num=float(input("Enter your number and we will check if your number is bigger than 0: " ))

if num > 0:
    print("შეყვანილი რიცხვი დადებითია")
elif num <0:
    print("შენი რიცხვი უარყოფითია")
elif num==0:
    print("თქვენი შეყვანილი რიხვი არც დადებითია და არც უარყოფითი")
else:
    print("სცადეთ თავიდან და შეიყვანეთ რიცხვი")

    #!!!!!!!!!!!!!!!!!!!!!!მეორე დავალებაშივე დავწერე ეს!!!!!!!!!!!!!!!!!!!!!#



# --------------------------------------    --------------------------------------    --------------------------------------    

# 6)დაწერეთ პროგრამა, რომლის მეშვეობითაც მომხმარებელი შეიყვანს 3 რიცხვს.
# იპოვეთ ამ რიცხვებს შორის ყველაზე პატარა და დაბეჭდეთ ეკრანზე (გამოიყენეთ if
# ოპერატორი).

num_first=float(input("Enter the first number here: "))
num_second=float(input("Enter the second number here: "))
num_third=float(input("Enter the third number here: "))

if num_first < num_second and num_first < num_third:
    print(num_first)
elif num_second < num_first and num_second < num_third:
    print(num_second)
elif num_third < num_first and num_third < num_second:
    print(num_third)
elif num_first==num_second and num_first < num_third:
    print(num_first , num_second , " ორივე ყველაზე პატარა რიცხვია")
elif num_first==num_third and num_first < num_second:
    print(num_first , num_third , " ორივე ყველაზე პატარა რიცხვია")
elif num_second==num_third and num_second < num_first:
    print(num_third , num_second , " ორივე ყველაზე პატარა რიცხვია")
elif num_first==num_second==num_third:
    print("სამივერი რიცხვი ტოლია ამიტომ სამივე არის ყველაზე პატარა")



# --------------------------------------    --------------------------------------    --------------------------------------    



# 7) იგივე პირობა რაც მე-6 სავარჯიშოს აქვს ოღონდ 4 რიცხვისთვის.
#აქ სხვა გზით დავწერ , რადგან პირობა ხელს მიწყობს და რამდენჯერ არის ეს პატარა რიცხვი აგარ დავწერ
num_a=float(input("Enter the first number here: "))
num_b=float(input("Enter the second number here: "))
num_c=float(input("Enter the third number here: "))
num_d=float(input("Enter the fourth number here: "))

if num_a<=num_b and num_a<=num_c and num_a<=num_d:
    print(num_a)
elif num_b<=num_a and num_b<=num_c and num_b<=num_d:
    print(num_b)
elif num_c<=num_a and num_c<=num_b and num_c<=num_d:
    print(num_c)    
else:
    print(num_d)




# --------------------------------------    --------------------------------------    --------------------------------------    



# 8) დაწერეთ პროგრამა, სადაც მომხმარებელი შეიყვანს
# ნებისმიერ რიცხვს 0-დან 100-ის ჩათვლით და
# შედეგად გამოიტანს შეფასების შესაბამის ლათინურ
# დასახელებას შემდეგი სქემის მიხედვით. მაგ.:
# თუ შეიტანს 45-ს, პროგრამამ უნდა დაბეჭდოს FX

grade=int(input("Enter your grade here (0-100): "))
if grade < 0 or grade>100:
    print("Enter the correct grade")
elif grade>=91 and grade<=100:
    print("A")
elif grade>=81 and grade<=90:
    print("B") 
elif grade>=71 and grade<=80:
    print("C")
elif grade>=61 and grade<=70:
    print("D")
elif grade>=51 and grade<=60:
    print("E")
elif grade>=41 and grade<=50:
    print("FX")
else:
    print("Failed")



# --------------------------------------    --------------------------------------    --------------------------------------    

# 9 ) დაწერეთ პროგრამა, რომლის მომხმარებელი შეიყვანს x ცვლადის ნებისმიერ რიცხვით მნიშვნელობას.
# გამოთვალეთ y ცვლადის მნიშვნელობა შემდეგი გამოსახულების მიხედვით და დაბეჭდეთ შედეგი.
x=float(input("Enter the x here: "))
if x > 0:
    print( "y wiil be --->" ,   ((x-9)**2) +   x/3    )
elif x<=0:
    print( "y wiil be --->" ,  (6+x**3) / 8 + 4*x     )
else:
    print("ENTER THE NUMBER")


# --------------------------------------    --------------------------------------    --------------------------------------    



# 10) დაწერეთ პროგრამა, რომლის მეშვეობით მომხმარებელი შეიყვანს x ცვლადის ნებისმიერ რიცხვით
# მნიშვნელობას. გამოთვალეთ y ცვლადის მნიშვნელობა შემდეგი გამოსახულების მიხედვით და დაბეჭდეთ
# შედეგი.

x_1=float(input("Enter the x here: "))
if x_1>0:
    print("y will be", 5+x_1**2)
elif x_1<0:
    print("y will be", (6-x_1)/(3+x_1))
elif x_1==0:
    print(6*x_1)
else:
    print("ENTER THE NUMBER")


# --------------------------------------    --------------------------------------    --------------------------------------    

# 11) დაწერეთ პროგრამა, რომლის გაშვებისას მომხმარებელი შეიყვანს ნებისმიერ რიცხვს.
# იპოვეთ შეყვანილი რიცხვის ბოლო ციფრი და დაბეჭდეთ ეკრანზე.

#ყველაზე მარტივი გზა $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
random_num=input("Enter the random number: ")
print(random_num[-1])

#მხოლოდ if elif else-ით
random_num_1=int(input("Enter the random number: "))
last_num=random_num_1 % 10
if last_num==0:
    print("0")
elif last_num==1:
    print("1")
elif last_num==2:
    print("2")
elif last_num==3:
    print("3")
elif last_num==4:
    print("4")
elif last_num==5:
    print("5")
elif last_num==6:
    print("6")
elif last_num==7:
    print("7")
elif last_num==8:
    print("8")
elif last_num==9:
    print("9")






# --------------------------------------    --------------------------------------    --------------------------------------    

# 12)
# დაწერეთ პროგრამა, რომლის მეშვეობითაც მომხმარებელი შეიყვანს რიცხვს.
# თუ შეყვანილი რიცხვი 3-ის ჯერადია, დაბეჭდეთ Fizz.
# თუ შეყვანილი რიცხვი 5-ის ჯერადია, დაბეჭდეთ Buzz.
# თუ რიცხვი ერთდროულად 3-ის და 5-ის ჯერადია, დაბეჭდეთ FizzBuzz.
# თუ რიცხვი არც 3-ის და არც 5-ის ჯერადი არ არის, დაბეჭდეთ თავად ეს რიცხვი.

num_3=int(input("Enter the number: "))
if num_3 % 3 == 0 and num_3 % 5==0:
    print("FizzBuzz")
elif num_3 % 3 == 0:
    print("Fizz")
elif num_3 % 5 == 0:
    print("Buzz")
else:
    print(num_3)


# --------------------------------------    --------------------------------------    --------------------------------------    


# 13)დაწერეთ პროგრამა, რომლის მეშვეობითაც მომხმარებელი შეიყვანს წელს და
# დაადგენთ არის თუ არა შეყვანილი რიცხვი ნაკიანი წელიწადი.
# მაგ.: 2012, 2016 წლები ნაკიანია.
# გაითვალისწინეთ, ნაკიანია წელიწადი, რომელიც უნაშთოდ იყოფა ოთხზე, გარდა იმ
# წლებისა რომლებიც იყოფა 100-ზე მაგრამ არ იყოფა 400-ზე. მაგ. 2100, 2200, 2300
# წლები არ არის ნაკიანი. 2000 წელი ნაკიანია.
year=int(input("Enter the any year you want and i will tell if it is a leap year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("it is a leap year")
else:
    print("it is not a leap year")