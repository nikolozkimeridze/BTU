# შექმენი ფუნქცია get_area(width, height), რომელიც მართკუთხედის ფართობს დააბრუნებს.
# შექმენი ფუნქცია get_perimeter(width, height), რომელიც მართკუთხედის პერიმეტრს დააბრუნებს.
# შექმენი ფუნქცია display_rectangle(width, height), რომელიც გამოიძახებს get_area()-სა და get_perimeter()-
# ს და ორივე შედეგს დაბეჭდავს. შეამოწმე სამი განსხვავებული მართკუთხედი.
width=float(input("Enter the width: "))
height=float(input("Enter the height: "))

def get_area(width, height):
    return width*height

def get_perimeter(width, height):
    return (width+height)*2

def display_rectangle(width, height):
    return get_area(width,height) , get_perimeter(width, height)
    
print(display_rectangle(width, height))