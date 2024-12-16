#!/usr/bin/python3

import re

password = input("Enter your password: ")

if (6 <= len(password) <= 12 and
    re.search("[a-z]", password) and
    re.search("[0-9]", password) and
    re.search("[A-Z]", password) and
    re.search("[$#@]", password)):
    print("Password is valid.")
else:
    print("Password is invalid.")













 