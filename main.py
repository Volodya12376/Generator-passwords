import random
import string

lenght = int(input("Write a lenght your password"))
numbers = input("You want password have a numbers.If yes:True")
symbols = input("You want password have a symbols.If yes:True")


def generate_password(length=lenght, digits=numbers, symbols=symbols):
    chars = string.ascii_letters
    if digits:
        chars = chars + string.digits
    if symbols:
        chars = chars + "!@#$%^&*"  

    password = ""

    for _ in range(length):
        password = password + random.choice(chars)

    return password

print("Password:    ", generate_password(lenght, digits=numbers, symbols=symbols))
