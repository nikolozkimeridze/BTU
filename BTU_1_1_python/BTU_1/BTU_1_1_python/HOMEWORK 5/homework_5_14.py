# შექმენი ფუნქცია print_items(item1, item2, separator=', '). მომხმარებელს შეეძლოს გამყოფის გადაცემა.

def print_items(item1, item2, separator=', '):
    print(item1 , separator , item2)

item1=input("Enter something here: ")
item2=input("Enter something here too: ")

print_items(item1 , item2)