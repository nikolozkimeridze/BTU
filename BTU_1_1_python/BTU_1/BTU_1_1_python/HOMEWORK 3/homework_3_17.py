# დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი.

prime=True
for j in range(2, 1001):
    for i in range(2,j):
        if j%i==0:
            prime=False
            break
        else:
            prime=True
    if prime:
        print(j)



# 2
# 2-3

# 3
# 2-4

# 4
# 2-5
