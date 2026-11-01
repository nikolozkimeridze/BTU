# შექმენი ფუნქცია countdown(start), რომელიც მოცემული რიცხვიდან 1-მდე დაბეჭდავს რიცხვებს და
# ბოლოს 'Go!'-ს.
def countdown(start):
    for i in range(start , 0 , -1):
# აქ მეწერა 1-მდე მაგრამ შემდეგ 0-მდე გავაკეთე უფრო ლამაზი ჩანდა
        print(i)
    print("Go!")
start=int(input("Enter the number here: "))
countdown(start)