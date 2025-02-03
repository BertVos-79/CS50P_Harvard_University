import sys
import os.path
from PIL import Image, ImageOps


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].lower().endswith((".jpg",".jpeg",".png")):
        sys.exit("Invalid input")
    elif not sys.argv[2].endswith((".jpg",".jpeg",".png")):
        sys.exit("Invalid output")
    elif os.path.splitext(sys.argv[1])[-1] != os.path.splitext(sys.argv[2])[-1]:
        sys.exit("Input and output have different extensions")
    else:
        try:
            image_before = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            size = shirt.size
            image_after = ImageOps.fit(image_before,size)
            image_after.paste(shirt,shirt)
            image_after.save(sys.argv[2])


        except FileNotFoundError:
            sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

