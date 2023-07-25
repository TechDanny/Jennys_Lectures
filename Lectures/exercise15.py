"""Find the maximum number in the list
"""

numbers = input("Enter numbers: ").split()
count = 0
for _ in numbers:
    count += 1
for i in range(count):
    numbers[i] = int(numbers[i])
print(f"the the new list with integers is:\n{numbers}")
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print(f"The maximum number is {max_number}")
