from pyfiglet import Figlet
import sys
import random

f = Figlet()
fonts = f.getFonts()


if len(sys.argv)==1:
    font = random.choice(fonts)
    f.setFont(font=font)
    s=input("Input: ")
    print(f.renderText(s))

elif len(sys.argv)==3:
    if sys.argv[1]not in ["-f","--font"]  or sys.argv[2] not in fonts:
         sys.exit("Invalid usage")

    font = sys.argv[2]
    f.setFont(font=font)
    s=input("Input: ")
    print(f.renderText(s))

else:
    sys.exit("Invalid usage")