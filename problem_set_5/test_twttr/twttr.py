def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    wrd = ""

    if not isinstance(word,str):
        raise TypeError("Input must be string")
    for char in word:
        if char.isalpha() and not char in "aeiouAEIOU":
            wrd += char

    return wrd


if __name__ == "__main__":
    main()
