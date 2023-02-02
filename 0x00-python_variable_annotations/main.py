#!/usr/bin/env python3

# Task 0 case
# add = __import__('0-add').add

# print(add(1.11, 2.22) == 1.11 + 2.22)
# print(add.__annotations__)

# Task 1 case
# concat = __import__('1-concat').concat

# str1 = "egg"
# str2 = "shell"

# print(concat(str1, str2) == "{}{}".format(str1, str2))
# print(concat.__annotations__)

# Task 2 case
import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))