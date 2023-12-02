def main():
    while True:
        date = get_outdate()
        if date is not None:
            print(f"{date[2]}-{date[0]:02}-{date[1]:02}")
            return

def get_outdate():
    month = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
    }

    while True:
        date = input("Date: ").strip().lower()
        if "/" in date:
            try:
                m, d, y = map(int, date.split("/"))
                if 1 <= m <= 12 and 1 <= d <= 31:
                    return m, d, y
            except ValueError:
                continue
        elif "," in date:
            try:
                m, d, y = date.replace(",","").split()
                m = m.lower()
                d = int(d)
                y = int(y)
                if m in month and 1 <= d <= 31:
                    return month[m], d, y
            except ValueError:
                continue

if __name__ =="__main__":
    main()