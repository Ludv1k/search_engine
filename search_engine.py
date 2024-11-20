import tkinter as tk
from tkinter import filedialog
import os

#Function to open file explorer and select a file
def choose_file():
    root = tk.Tk()      #Create the main tkinter window
    root.withdraw()     #Hide the blank tkinter window

    initial_directory = os.path.abspath("short_stories") #Converts to an absolute path

    file_path = filedialog.askopenfilename(
        title="Select a text file",             #Title of the file dialog
        initialdir=initial_directory,           #Open Directly to the "short_stories" folder
        filetypes=[("Text files", "*.txt")]     #Only show .txt files
    )
    return file_path    #Return the selected file's path

#Get the file path using the file explorer
textfile = choose_file()
#Ask the user for the word to search
seek = input("What do you want to find? ").lower()

#Function to read and search the text
def readText(textfile):
    with open(textfile, "rt") as f:     #Open the selected file
        text = f.read().lower()         #Read and convert text to lowercase
    Amount = text.count(seek)           #Count amount of times the word appears
    if seek in text:                    #Check if the word exists
        print("The word '" + seek + "' is in the text. And it was found", Amount, "times.")
    else:
        print("The word", seek, "is not featured in the text.")

if textfile:                      #Ensure a file was selected
    readText(textfile)
else:
    print("No file selected.")    #Handle case where no file was chosen
