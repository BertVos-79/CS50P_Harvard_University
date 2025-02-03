import sys
import random
import pyfiglet


def main():
    figletize()


def figletize():
    figlet = pyfiglet.Figlet()

    if len(sys.argv) == 1:
        fname = random.choice(figlet.getFonts())
        figlet.setFont(font=fname)

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid font name")

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
