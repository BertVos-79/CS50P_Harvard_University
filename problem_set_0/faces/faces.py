def convert(phrase):
    c_phrase = phrase.replace(":)", "🙂").replace(":(", "🙁")
    return c_phrase


def main():
    phrase = convert(input("So, how are you doing these days?\n"))
    print(phrase)


main()




