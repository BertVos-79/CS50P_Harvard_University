def main():
    adieu()


def adieu():
    import inflect

    names = []
    p = inflect.engine()

    while True:

        try:
            name = input("Name: ")
            names.append(name)

        except EOFError:
            print(f"Adieu, adieu, to {p.join(names)}")
            return


if __name__ == "__main__":
    main()
