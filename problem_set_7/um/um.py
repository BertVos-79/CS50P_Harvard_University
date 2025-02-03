import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(\b[uU][mM]\b)+"
    counter = re.findall(pattern,s)
    return len(counter)



if __name__ == "__main__":
    main()

