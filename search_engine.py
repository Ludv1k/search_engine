textfile = "textfile.txt"
seek = input("What do you want to find? ")

def readText(textfile):
    f = open(textfile, "rt")
    teksten = (f.read())
    teksten = teksten.lower()
    if seek in teksten:
        print("true")
    else:
        print("false")

readText(textfile)