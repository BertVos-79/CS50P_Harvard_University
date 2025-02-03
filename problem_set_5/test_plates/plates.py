def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not start(s):
        return False
    if not length(s):
        return False
    if not number(s):
        return False
    if not sign(s):
        return False
    return True


def start(s):
    if s[0:1].isalpha():
        return True


def length(s):
    if 1 < len(s) < 7:
        return True


def number(s):
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif number_started:
            return False
    return True


def sign(s):
    for char in s:
        if char not in ". ,":
            return True


if __name__ == "__main__":
    main()
