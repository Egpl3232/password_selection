import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@$&*_-"

user_for = lower_case + upper_case + number + symbols
for_pass = 8

password = "".join(random.sample(user_for, for_pass))

print("Ваш пароль:", password)