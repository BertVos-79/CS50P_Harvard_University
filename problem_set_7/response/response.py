from validator_collection import validators


try:
    mail = validators.email(input("What's your email address? "))
    print("Valid")
except ValueError:
    print("Invalid")
