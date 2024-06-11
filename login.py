#!/usr/bin/env python3

while True:
    email = input("Enter email: ")
    if email == "ramackersjp@outlook.com":
        print("Address found")
        break
    else:
        print("Address not found, please try again.")

password = input("Enter password: ")
if password == "1234":
    print("Welcome")
else:
    print("Wrong")
