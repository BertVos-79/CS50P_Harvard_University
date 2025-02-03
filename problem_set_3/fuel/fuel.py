def main():
    print(fuel())


def fuel():
    while True:
        fraction_str = input("Enter a fraction of two integers in the format 'x/y': ")
        fraction_lst = fraction_str.split("/")

        try:
            fuel = round((int(fraction_lst[0])/int(fraction_lst[1])) * 100)
        except (ValueError, ZeroDivisionError):
            continue

        if fuel > 100:
            continue
        elif fuel <= 1:
            return ("E")
        elif fuel >= 99:
            return ("F")
        else:
            return (f"{fuel}%")

main()
