def main():
     print(get_percent())

def get_percent():
    while True:
        try:
            fraction=input("Fraction: ")
            x,y=fraction.split('/')
            x=float(x)
            y=float(y)
            if not x.is_integer() or not y.is_integer() or x>y or y==0:
                continue
            percentage=(x/y)*100
            if percentage<=1:
                    return 'E'
            if percentage>=99:
                    return 'F'
            return f"{round(percentage)}%"
        except (ValueError, ZeroDivisionError):
            pass

main()