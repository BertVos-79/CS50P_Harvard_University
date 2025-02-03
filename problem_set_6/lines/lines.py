import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")

        with open(sys.argv[1]) as file:
            print(counter(file))

    except FileNotFoundError:
        sys.exit("File does not exist")


def counter(file):
    count = 0
    for line in file:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        else:
            count += 1
    return count


if __name__ == "__main__":
    main()
