def main():
    print(f"Output: {strng()}")


def strng():
    string = input("Input: ")
    strng = ""

    for char in string:
        if not char in "aeiouAEIOU":
            strng += char

    return strng

main()
