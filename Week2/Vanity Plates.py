def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    for i in range(2,len(s)):
        if s[i].isnumeric():
            if s[i]=='0' and i==2:
                return False
            for j in range(i+1,len(s)):
                if not s[j].isnumeric():
                    return False
    return True


main()