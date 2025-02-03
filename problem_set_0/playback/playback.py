def playback():
    message = input("Please, enter your message here: ").replace(" ", "...")
    return message


def main():
    print(playback())


main()
