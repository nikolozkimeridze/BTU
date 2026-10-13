#1. რომელი შეიძლება იყოს ცვლადის სახელი?

#a) name                l) x2
#b) x                   m) სახელი
#c) 2x                  n) $14
#d) total_sum           o) __name
#e) totalSum            p) _6
#f) total sum           q) ___
#g) totalsum            r) 14%
#h) total-sum           s) k1427
#i) total.sum           t) While
#j) if                  u) sum
#k) true

# a , b , d , e , g ,k(დიდი T თუ იქნება არა),  l , m , o , p , q , s , t(პატარა W თუ იქნება არა) , u 



#2) ა)  5+3*3*3 - 4 * 6*6/13 +5*5*5

print((5+3**3)-(4*6*6/13)+5**3)

#2)  ბ)  (89-15*3)/(17-√25)

print((89-15*3)/(17-25**(1/2)))


#2)  გ) (55+125)* 6 -7*7*7

res=55+125
res=res*6
res=res-7**3
print(res)



#2)  დ) I (13-35)/7 I დაამრგვალეთ ასეულებამდე

res_1=(13-35)/7
res_1=res_1+ (-2)*res_1 # ან res_1 = res_1 - 2 * res_1
print(round(res_1 , 2))


#2)   ე)  (3 ხარისხად ფესვი3 ((3*7*8)) +2) / (5+ ფესვი 2 ხარისხად 3 (5*183))
row_1=3**((3*7*8)**(1/3)) + 2
row_2=5+ (5*183)**(1/(2**3))
print(row_1/row_2)


#3დაწერეთ პროგრამა, რომელიც message ცვლადს მიანიჭებს ტექსტს: "Hello World!" და შემდეგ დაბეჭდეთ message ცვლადი.

mes="Hello World"
print(mes)

#4შექმენით ორი ცვლადი: a-ს მიანიჭეთ 2, ხოლო b-ს მიანიჭეთ 7. გაუცვალეთ a-ს და b-ს მნიშვნელობები (ეცადეთ მოიფიქროთ რამდენიმე ამოხსნის გზა).
#მთავარი გზა
a_1=2
b_1=7
print(a_1 , b_1)
a_1 , b_1 = b_1 , a_1
print(a_1 , b_1)
                            #  ----------გზა 1------------
a=2
b=7
print("როგორი იყო a და b - >" , a , b)
a=b
b=a-5
print("როგორი გახდა a და b - >",a, b)
                            #   -----------გზა 2-----------
                #ვთვათ a არის x და b y რადგან სხვა სახელის ცვლადები იყოს

x=2
y=7
print("როგორი იყო x და y- >" , x , y)
x=x**3-1
y=x+y-12
print("როგორი გახდა x და y - >" , x , y)
                            #   -----------გზა 3-----------
        #ვთვათ a არის z და b c რადგან სხვა სახელის ცვლადები იყოს ყველაზე პრიმიტიული გზა

z=2
c=7
print("როგორი იყო z და c- >" , z , c)
z=z**3-1
c=z+c-12
print("როგორი გახდა z და c - >" , z , c)

            

#5დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება სახელსა და გვარს. შემდეგ ერთ ხაზზე დაბეჭდეთ სახელი და გვარი.

name=input("Enter your name here: ")
surname=input("Enter your surname here: ")
print(name , surname)

#.6დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შეყვანილ რიცხვს გადაიყვანს ორობითში, რვაობითსა და თექვსმეტობითში.
system_ques=int(input("Enter the number you want transfer into 2,8,16 number systems: "))      #??????? float რატომ არ მუშაობს??? ხომ შეიძლება რომ არამთელი რიცხვიც     გადავიყვანოთ და უსასრულობაში წავა გადაყვანა და პროგრამა უბრალოდ დაამრგვალებს?????????????
print(bin(system_ques))
print(oct(system_ques))
print(hex(system_ques))

#.7დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება თვეში სამუშაო საათების რაოდენობასა და საათობრივ ანაზღაურებას. გამოთვალეთ და დაბეჭდეთ მომხმარებლის ყოველთვიური ხელფასი.
hours=float(input("How many hours do you work in a month? : "))
sal_per_h=float(input("How much do you make in a hour? : "))
sum=hours*sal_per_h
print("So it is your salary :" , sum)

#8. დაწერეთ პროგრამა, სადაც მომხმარებელი შეიყვანს 5 რიცხვს და პროგრამა გამოითვლის მათ საშუალო არითმეტიკულს.

q_1=float(input("Enter the first number: "))
q_2=float(input("Enter the second number: "))
q_3=float(input("Enter the third number: "))
q_4=float(input("Enter the fourth number: "))
q_5=float(input("Enter the fifth number: "))
sum_1=(q_1+q_2+q_3+q_4+q_5)/5
print("საშუალო არითმეტიკული შენი ჩაწერილი რიცხვების არის - >", sum_1)

#9. დაწერეთ პროგრამა, რომელშიც მომხმარებელი შეიყვანს თამაშის ჯამური წუთების რაოდენობას. პროგრამა გამოითვლის და დაბეჭდავს საათებისა და წუთების #რაოდენობას. (მაგ.: 125 წთ -> 2 სთ 5 წთ)

mins=float(input("Enter minutes that you have played the game: "))
hour=0
mins_left=0
if mins >= 60:
    hour=mins//60
    mins_left=mins-(hour*60)
    print(hour , "საათი და", mins_left , "წუთი")
else:
    print(mins , "წუთი")

                                        #--------------------სხვა გზა--------------------
mi=float(input("Enter minutes that you have played the game: ")) 
a=mi//60
print(a, "საათი და",mi-(60*a), "წუთი" )                                     



#10. დაწერეთ 2 პროგრამა, რომელიც მომხმარებლის მიერ შეყვანილ ტემპერატურას გადაიყვანს ცელსიუსიდან ფარენჰეიტში და პირიქით. გადაყვანის ფორმულები:
            #  I პროგრამა ფარენგეიტი--->>>ცელსიუსი
ques_1=float(input("Enter degree in celsius to transfer it into fahrenheit: "))
print("in fahrenheit it will be: ", ques_1*9/5 +32 ,"F")
            #  II პროგრამა ფარენგეიტი--->>>ცელსიუსი
ques_2=float(input("Enter degree in fahrenheit to transfer it into celsius: "))
print("in celsius it will be: ", 5/9*(ques_2-32), "C")

            #სხვა გზა კიდევ
ques_3=input("Enter what you want to transfer?? fahrenheit to celsius OR celsius to fahrenheit: ")
if ques_3=="fahrenheit to celsius":
    ques_4=float(input("Enter degree in fahrenheit to transfer it into celsius: "))
    print("in celsius it will be: ", 5/9*(ques_4-32) , "C")
elif ques_3=="celsius to fahrenheit":
    ques_5=float(input("Enter degree in celsius to transfer it into fahrenheit: "))
    print("in fahrenheit it will be: ", ques_5*9/5 +32 ,"F")
else:
    print("check if you typed the correct words and try again")