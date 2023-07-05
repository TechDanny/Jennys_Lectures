"""Love calculator"""
my_name = input("What is your name? ").lower()
partner_name = input("What is his/her name? ").lower()
concat_name = my_name + partner_name
t = concat_name.count("t")
r = concat_name.count("r")
u = concat_name.count("u")
e = concat_name.count("e")
true = t + r + u + e

l = concat_name.count("l")
o = concat_name.count("o")
v = concat_name.count("v")
e = concat_name.count("e")
love = l + o + v + e

total_love = str(true) + str(love)
print(f"Your Love in percentage is {total_love}%")
