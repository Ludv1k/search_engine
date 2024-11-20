textfile = "textfile.txt"
seek = input("What do you want to find? ").lower()

def readText(textfile):
    f = open(textfile, "rt")
    text = (f.read())
    text = text.lower()
    Amount = text.count(seek)
    if seek in text:
        print("true")
        print(Amount)
    else:
        print("false")

readText(textfile)