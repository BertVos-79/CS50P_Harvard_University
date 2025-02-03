def main():
    change()


def change():
    amount = 50

    while True:
        coin = int(input("Please, enter a coin of 5, 10 or 25 cents\n"))

        match coin:
            case 5|10|25:

                amount -= coin

                if amount > 0:
                    print(f"Amount Due: {amount}")
                elif amount < 0:
                    print(f"Change Owed: {-(amount)}")
                    break
                else:
                    print(f"Change Owed: {amount}")
                    break
            case _:
                print(f"Amount Due: {amount}")

main()


