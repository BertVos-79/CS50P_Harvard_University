import sys
import csv
from tabulate import tabulate


def main():

    print(csv_to_table())


def csv_to_table():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                file = csv.reader(file)
                return tabulate(file, headers="firstrow", tablefmt="grid")

        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
