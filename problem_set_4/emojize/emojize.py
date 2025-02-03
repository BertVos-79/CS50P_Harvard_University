import emoji


def main():
    emojize()


def emojize():
    print(f"Output: {emoji.emojize(input("Input: "),language='alias')}")
    return


main()
