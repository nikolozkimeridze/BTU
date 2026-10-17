# დაწერეთ პროგრამა რომელიც ეკრანზე გამოიტანს შემდეგ გამოსახულებებს.


# ------------------------------------------------------------------------------------

# A

# print("* * * * * *")
# print("*         *")
# print("*         *")
# print("* * * * * *")
# print("*         *")
# print("*         *")
# print("* * * * * *")




# print("* * * * * *")      აქ თავიდან ესეც მეწერა არ ვიცოდი რომ 0 % 3-ზე ==0 იყო პითონში
for i in range(7):
    if i % 3 == 0:
        print("* * * * * *")
    else:
        print("*         *")

# ------------------------------------------------------------------------------------

#B

# ------------------------------------------------------------------------------------

# print("*")
# print("* *")
# print("* * *")
# print("* * * *")
# print("* * *")
# print("* *")
# print("*")

for x in range(0, 4):
    print(x * "*")
for b in range (4 , 0 , -1):
    print(b * "*")



# ------------------------------------------------------------------------------------

#C
#9

# for k in range(-1,8, 2):
#     k+=2
#     print(k*"*")
#     k=k-2
#ესე ვერ მოვიფიქრე რა დამემატებინა


#სხვანაირად
height = 5
for k in range(height):
    space= " " * (height-k-1)
    star="*" * (2 * k + 1)
    print(space + star)




# ------------------------------------------------------------------------------------

#D
#NIKA

#N

# print("*     *")
# print("**    *")
# print("* *   *")
# print("*  *  *")
# print("*   * *")
# print("*    **")


# first_height=5
# print("*     *")
# for n in range(first_height):
#     first_space=" " * (first_height - n - 5)
#     first_star="*" + first_space +"*"
#     print(first_star)
#ესე არ გამომივიდა
#სხვა გზით

print("*     *")
for n in range(1,6):
    first_space= " "  * (n-1)
    second_space= " " * (5-n)
    print("*" +first_space + "*" + second_space + "*")



# I
# print("*******")
# print("   *   ")
# print("   *   ")
# print("   *   ")
# print("   *   ")
# print("*******")
print("*******")
for e in range(4):
    print(" "* 3 + "*"+ 3* " ")
print("*******")


#K
# print("*   *")
# print("*  * ")
# print("* *  ")
# print("**   ")
# print("* *  ")
# print("*  * ")
# print("*   *")
for p in range(1,8):
    while p <=4:
        space1=" "*(4-p)
        space2=" "*(p+1)
        print("*"+ space1 + "*")
        break
    while p> 4 and p<8:
        spacee1=" " * (p-4)
        spacee2=" " * (p-3)    
        print("*"+ spacee1 + "*")
        break
    

# #A
# print("    *    ")
# print("   * *   ")
# print("  *****  ")
# print(" *     * ")
for a in range(1,5):
    space_a=" " * (5-a)
    while a==1:
        print(space_a + "*")
        break
    while a==2:
        print(space_a + "*" + " " + "*")
        break
    while a==3:
        print(space_a + "*****")
        break
    while a==4:
        print(space_a + "*" + "     " + "*")
        break
#აქ A ცოტა გამოწეულია სხვებთან შედარებით მარა აღარ დავუმატე ყველას  " " 

    