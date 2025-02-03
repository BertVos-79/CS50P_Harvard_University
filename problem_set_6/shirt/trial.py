import sys
from PIL import Image, ImageOps

def main():
    # Open the input image and shirt image
    image_before = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    # Resize the input image to the size of the shirt
    size = shirt.size
    print(f"Shirt size: {size}")  # This should be (600, 600)

    # Fit the input image to match the size of the shirt
    image_before = ImageOps.fit(image_before, size)
    print(f"Resized input image size: {image_before.size}")  # This should match the shirt size

    # Paste the shirt onto the resized input image
    image_before.paste(shirt, (0, 0), shirt)

    # Save the final output
    image_before.save("output.jpg")

if __name__ == "__main__":
    main()
