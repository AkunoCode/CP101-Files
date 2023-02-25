"""
Check for the validity of an email
An email has three parts:
1. The local part or the part before the @ symbol
2. The Domain name
3. Host Name
"""
import re

email = input("Enter your email: ")


def splitByAt(email):
    if email.count("@") == 1:
        checkDotDNS(email.split("@"))
    else:
        print("Invalid Email")


def checkDotDNS(email):
    if email[-1].count(".") == 1:
        email[-1] = email[-1].split(".")
        characterChecking(email)
    else:
        print("Invalid Email")


def characterChecking(email):
    validity = []
    if re.match(r"^[\w\.]+$", email[0]):
        validity.append(True)
    else:
        validity.append(False)

    if email[1][0].isalnum() and len(email[1][1]) >= 2:
        validity.append(True)
    else:
        validity.append(False)

    if email[1][1].isalnum() and len(email[1][1]) >= 2:
        validity.append(True)
    else:
        validity.append(False)

    if False in validity:
        print("Invalid Email")
    else:
        print("Valid Email")


splitByAt(email)
