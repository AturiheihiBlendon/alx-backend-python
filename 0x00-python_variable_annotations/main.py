#!/usr/bin/env python3

# Task 0 case
# add = __import__('0-add').add

# print(add(1.11, 2.22) == 1.11 + 2.22)
# print(add.__annotations__)

# Task 1 case
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
