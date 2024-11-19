textfile = "textfile.txt"
seek = input("What do you want to find? ")

def readText(textfile):
    f = open(textfile, "rt")
    print(f.read())

readText(textfile)