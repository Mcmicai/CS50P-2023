def main():
    print(get_total())

def get_total():
    total=0
    d_orig={
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    d={}
    for key,value in d_orig.items():
        d[key.lower()]=value
    while True:
        try:
            item = input("Item: ").lower()
            if item in d:
                total+=d[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            break
    return f"Total: ${total:.2f}"

main()