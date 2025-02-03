def einstein_converter(weight):
    energy = weight * (300000000**2)
    return energy


def main():
    energy = einstein_converter(int(input("Enter a mass in kilograms: ")))
    print(f"According to Einstein's Theory of Relativity this is equal to {energy:,} of Joules.")


main()
