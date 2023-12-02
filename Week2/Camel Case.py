def convert(name):
    return ''.join(['_' +i.lower() if i.isupper() else i for i in name])

name=input(" ")
print(convert(name))