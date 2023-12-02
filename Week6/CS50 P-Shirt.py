import sys
from PIL import Image,ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input=sys.argv[1]
output=sys.argv[2]
types=(".jpg",".jpeg",".png")

if not output.endswith(types):
    sys.exit("Invalid output")
elif input.split(".")[1] != output.split(".")[1]:
    sys.exit("Input and output have different extensions")

shirt=Image.open("shirt.png")

try:
    with Image.open(input) as im:
        im=ImageOps.fit(im,shirt.size)
        im.paste(shirt,shirt)
        im.save(output)
except FileNotFoundError:
    sys.exit("Input does not exist")