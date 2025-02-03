def main():
    time = input("What time is it? ").strip()
    meal(convert(time))


def convert(time):
    time_list = time.split(":")
    time_float = round(float(time_list[0]) + (float(time_list[1])*0.0166666666667),2)
    return time_float

def meal(time):
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
