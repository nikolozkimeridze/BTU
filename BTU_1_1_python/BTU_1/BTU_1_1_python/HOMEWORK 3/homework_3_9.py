# დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue ოპერატორი.

#150-mde
total=0
for i in range(15 , 150):
    if i == 50 or i == 75 or i == 80:
        continue
    else:
        total += i
print(total)
