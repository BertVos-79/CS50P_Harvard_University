from random import randint


def main():
    print(guess())


def guess():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
            else:
                number = randint(1, n)

                while True:
                    try:
                        guess = int(input("Guess: "))
                        if guess < 1:
                            continue
                        elif guess < number:
                            print("Too small!")
                            continue
                        elif guess > number:
                            print("Too large!")
                            continue
                        else:
                            return "Just right!"

                    except (ValueError, TypeError):
                        continue

        except (ValueError, TypeError):
            continue


if __name__ == "__main__":
    main()
