def main():
    greeting = input("Hello there, I have a question about my account.").lstrip().lower()
    print(f"Greeting: {greeting}")
    renumeration(greeting)

def renumeration(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
