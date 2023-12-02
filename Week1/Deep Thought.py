n = input("What is the Answer to the Great Question of Life,the Universe, and Everything? ").strip()

if n =="42" or n.lower()=="forty-two" or n.replace(" ","").lower()=="fortytwo":
    print("Yes")
else:
    print("No")