import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:

            with open(sys.argv[1], "r") as before_file, open(
                sys.argv[2], "w", newline=""
            ) as after_file:
                reader = csv.DictReader(before_file)

                writer = csv.DictWriter(
                    after_file, fieldnames=["first", "last", "house"]
                )
                writer.writeheader()

                for row in reader:

                    last, first = row["name"].split(",")

                    writer.writerow(
                        {
                            "first": first.strip(),
                            "last": last.strip(),
                            "house": row["house"].strip(),
                        }
                    )
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
