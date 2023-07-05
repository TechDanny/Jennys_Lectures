print("=====PIZZA ORDER PROGRAM=====")
print()
print("====================")
print()
print()
print("       MENU        ")
print()
print()
print("====================")
print()
print("1. Small pizza = 100\n2. Medium pizza = 200\n3. Large pizza = 300")
print()
print("=====EXTRA TOPPINGS=====")
print()
print("1. Pepperoni for small pizza = 30\n2. Pepperoni for medium or large pizza = 50")
print()
options = int(input("Hello, which order would you love place? "))
large_pizza = 300
total = 0
if options == 1:
    small_pizza = 100
    extra = input("would you love we add pepperoni [Y/N]: ")
    if extra == "y".lower():
        total = small_pizza + 30
        print(f"Your bill is {total}")
    else:
        print(f"Your bill is {small_pizza}")
elif options == 2:
    medium_pizza = 200
    extra = input("Would you love we add pepperoni [Y/N]: ")
    if extra == "y".lower():
        total = medium_pizza + 50
        print(f"Your bill is {total}")
    else:
        print(f"Your bill is {medium_pizza}")
elif options == 3:
    large_pizza = 300
    extra = input("Would you love we add pepperoni [Y/N]: ")
    if extra == "y".lower():
        total = large_pizza + 50
        print(f"Your bill is {total}")
    else:
        print(f"Your bill is {large_pizza}")
else:
    print("Please choose the correct option")

print()
print("Thank you for ordering with us")
