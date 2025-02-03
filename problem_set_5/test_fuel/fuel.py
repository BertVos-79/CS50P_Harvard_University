def main():
    fraction = input("Enter a fraction of two integers in the format 'x/y': ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        if x > y:
            raise ValueError("X cannot be greater than Y.")

        percentage = round((x / y) * 100)
        return percentage

    except ValueError:
        raise ValueError("Invalid input. X and Y must be integers.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

