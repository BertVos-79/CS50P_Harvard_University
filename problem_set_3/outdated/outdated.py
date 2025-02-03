def main():
    date_converter()


def date_converter():
    months = [
               "January",
               "February",
               "March",
               "April",
               "May",
               "June",
               "July",
               "August",
               "September",
               "October",
               "November",
               "December"
            ]

    while True:
        date_mdy = input("Date: ")

        try:
            if "/" in date_mdy:
                date_list = date_mdy.split("/")
                if int(date_list[0]) > 12 or int(date_list[1]) > 31:
                    continue
                else:
                    print(f"{int(date_list[2]):02}-{int(date_list[0]):02}-{int(date_list[1]):02}")
                    return

            elif "," not in date_mdy:
                continue

            else:
                date_mdy = date_mdy.replace(",", "")
                date_list = date_mdy.split()
                for month in months:
                    if month == date_list[0]:
                        date_list[0] = months.index(month) + 1
                if int(date_list[0]) > 12 or int(date_list[1]) > 31:
                    continue
                else:
                    print(f"{int(date_list[2]):02}-{int(date_list[0]):02}-{int(date_list[1]):02}")
                    return

        except ValueError:
            pass


main()
