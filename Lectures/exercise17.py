"""
FizzBuzz job interview Questions
"""

for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print(f"{numbers}: FizzBuzz")
    elif numbers % 3 == 0:
        print(f"{numbers}: Fizz")
    elif numbers % 5 == 0:
        print(f"{numbers}: Buzz")
    elif not numbers % 3 == 0 and not numbers % 5 == 0:
        print(numbers)
