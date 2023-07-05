import random
name = input("Enter everybody's name separated by a comma: ").split(", ")
pay_bill = random.choice(name)
print(name)
print()
print(f"{pay_bill} will pay the bill")
