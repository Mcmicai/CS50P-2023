def main():
    str = input("")
    r = convert(str)
    print(r)

def convert(n):
    c = n.replace(":)" ,"🙂").replace(":(" ,"🙁")
    return c

main()