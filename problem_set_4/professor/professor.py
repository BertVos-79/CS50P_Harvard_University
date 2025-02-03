from random import randint


def main():
    print(f"Score: {generate_integer(get_level())}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
            else:
                continue
        except ValueError:
            continue


def generate_integer(n):
    if n == 1:
        score = 0

        for _ in range(10):
            trial = 0
            x = randint(0, 9)
            y = randint(0, 9)
            sum = x + y

            while trial < 3:
                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                    trial += 1
                    continue

                if answer != sum:
                    print("EEE")
                    trial += 1
                else:
                    score += 1
                    break

            if trial == 3:
                print(f"{x} + {y} = {sum}")

        return score

    elif n == 2:
        score = 0

        for _ in range(10):
            trial = 0
            x = randint(10, 99)
            y = randint(10, 99)
            sum = x + y

            while trial < 3:
                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                    trial += 1
                    continue

                if answer != sum:
                    print("EEE")
                    trial += 1

                else:
                    score += 1
                    break

            if trial == 3:
                print(f"{x} + {y} = {sum}")

        return score

    else:
        score = 0

        for _ in range(10):
            trial = 0
            x = randint(100, 999)
            y = randint(100, 999)
            sum = x + y

            while trial < 3:

                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                    trial += 1
                    continue

                if answer != sum:
                    print("EEE")
                    trial += 1
                else:
                    score += 1
                    break

            if trial == 3:
                print(f"{x} + {y} = {sum}")

        return score


if __name__ == "__main__":
    main()
