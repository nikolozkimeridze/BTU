# შექმენი ფუნქცია celsius_to_fahrenheit(celsius), რომელიც ცელსიუსებში მოცემულ ტემპერატურას
# ფარენჰეიტებში გადაიყვანს.
# ფორმულა:
# F= C * 9/5 + 32

def celsius_to_fahrenheit(celsius):
    print("In F it will be" , ((celsius * 9) / 5) + 32 )

celsius1=float(input("Enter degree in celsius: "))
celsius_to_fahrenheit(celsius1)