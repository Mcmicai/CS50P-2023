def main():
    Amount=50
    print(f"Amount Due: {Amount}")
    while Amount>0:
        coin=Insert()
        if coin not in [5,10,25]:
            print(f"Amount Due: {Amount}")
            continue
        Amount-=coin
        if Amount>0:
            print(f"Amount Due: {Amount}")

        if Amount ==0:
            print("Change Owed: 0")
        else:
            print(f"Change Owed: {abs(Amount)}")


def Insert():
    return int(input("Insert Coin: "))

main()