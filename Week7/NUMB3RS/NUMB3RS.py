import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip):
        return False
    for i in ip.split("."):
        if int(i)<0 or int(i)>255:
            return False
    return True


if __name__ == "__main__":
    main()