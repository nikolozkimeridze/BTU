# შექმენი ფუნქცია calculate_age(birth_year), რომელიც გამოთვლის და დააბრუნებს ასაკს, შემდეგ
# დაბეჭდეთ.

 # თვეს და დღეს დავამატებ რომ უფრო ზუსტი იყოს
birth_year1=int(input("Enter the year you were born: "))
question_1=int(input("Enter which month you were born: 1/2/3/4/5/6/7/8/9/10/11/12: "))
question_2=int(input("Enter which day you were born: 1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30: "))

def calculate_age(birth_year, birth_month , birth_day):
    if  question_1 < 10:
        print(2026-birth_year ," წლის ხარ")
        #29-რიცხვში ვწერ და მაგიტომ მაქვს birth_month 29
    elif question_1==10 and birth_month<=29:
        print(2026-birth_year," წლის ხარ")
    else:
        print(2026-birth_year-1," წლის ხარ")
calculate_age(birth_year1 , question_1 , question_2)
