import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"([1-9]|1[0-2]):?([0-5][0-9])? ([AP])M to ([1-9]|1[0-2]):?([0-5][0-9])? ([AP])M"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    start_hour = int(match.group(1))
    start_minutes = match.group(2) if match.group(2) else "00"
    start_period = match.group(3)

    end_hour = int(match.group(4))
    end_minutes = match.group(5) if match.group(5) else "00"
    end_period = match.group(6)

    start_hour = convert_to_24_hour(start_hour, start_period)
    end_hour = convert_to_24_hour(end_hour, end_period)

    return f"{start_hour:02}:{start_minutes} to {end_hour:02}:{end_minutes}"


def convert_to_24_hour(hour, period):
    if period == "A":
        if hour == 12:
            return 0
    else:
        if hour != 12:
            return hour + 12
    return hour


if __name__ == "__main__":
    main()
