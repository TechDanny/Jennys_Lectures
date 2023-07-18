"""
A program to calculate average height from a list of heights,
take input from the user
"""

heights = []
total_height = 0
n = int(input("Enter the size of the list: "))
for height in range(n):
    each_height = int(input(f"Enter height{height + 1}: "))
    heights.append(each_height)
else:
    for num in heights:
        total_height += num
        average_height = total_height / n
    print(round(average_height))
