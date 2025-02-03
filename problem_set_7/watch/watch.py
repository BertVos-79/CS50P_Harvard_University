import re

def main():
    print(parse(input("HTML: ")))

def parse(html):
    pattern = r'<iframe .*src="https?://(?:www\.)?youtube\.com/embed/([\w]{11})".*</iframe>'
    match = re.search(pattern, html)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
