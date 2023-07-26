"""
This is a mini password generator programmed with python
"""
import random

print("Welcome to the Password Generator!")
total_letters = int(input("How many letters would you want in your password? "))
total_symbols = int(input("How many Symbols would you want? "))
total_numbers = int(input("How many numbers would you want? "))
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
           "u", "v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
           "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols = ["!","@","#","$","%","^","&","*","(",")"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
password =[]
my_password = ""
for _ in range(1, total_letters+1):
    char = random.choice(letters)
    password += char
for _ in range(1, total_symbols+1):
    symb = random.choice(symbols)
    password += symb
for _ in range(1, total_numbers+1):
    num = random.choice(numbers)
    password += num
random.shuffle(password)
for i in password:
    my_password += i
print(my_password)




