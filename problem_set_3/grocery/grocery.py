def main():
    grocery()


def grocery():
    grocery_lst = {}

    while True:

        try:
            item = input().lower()

            if not item in grocery_lst:
                grocery_lst[item] = 1
            else:
                grocery_lst[item] += 1

        except KeyError:
            pass

        except EOFError:
            print("\n")
            break

    for item in sorted(grocery_lst):
        print(grocery_lst[item],item.upper())

main()
