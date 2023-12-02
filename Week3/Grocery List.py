def main():
    grocery={}
    while True:
        try:
            item = input(" ").lower()
            if item in grocery:
                grocery[item]+=1
            else:
                grocery[item]=1
        except EOFError:
            break
    for item in sorted(grocery.keys()):
        print(f"{grocery[item]} {item.upper()}")

if __name__=="__main__":
    main()