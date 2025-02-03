from datetime import date
import inflect
import sys


def get_total_minutes(birth_date, today):
    return (today - birth_date).days * 24 * 60


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth (YYYY-MM-DD): "))
    except ValueError:
        sys.exit("Invalid input. Please enter a valid date in the format YYYY-MM-DD.")

    total_minutes = get_total_minutes(birth_date, date.today())

    p = inflect.engine()
    minutes_in_words = p.number_to_words(total_minutes, andword="").capitalize()
    minute_word = p.plural("minute", total_minutes)

    print(f"{minutes_in_words} {minute_word}")


if __name__ == "__main__":
    main()
