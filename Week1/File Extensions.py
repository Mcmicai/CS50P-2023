str = input("Greeting: ").lower().strip()

if str.startswith("hello"):
    print("$0")

elif str.startswith("h"):
    print("$20")

else:
    print("$100")