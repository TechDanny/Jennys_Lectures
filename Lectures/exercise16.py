"""
calculate the sum of even numbers between 1 to 100
"""

total = 0
for numbers in range(1, 101):
    if numbers % 2 == 0:
        total += numbers
print(total)
