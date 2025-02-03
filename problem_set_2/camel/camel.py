def main():
    print(snake())


def snake():
    camel = input("Input your filename in camelCase here: ")
    snake = ""

    for letter in camel:
        if not letter.islower():
            snake += "_" + letter.lower()
        else:
            snake += letter

    return snake


main()


