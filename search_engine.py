import tkinter as tk
from tkinter import filedialog

# Function to open file explorer and select a file
def choose_file():
    root = tk.Tk()               # Create the main tkinter window
    root.withdraw()              # Hide the blank tkinter window

    file_path = filedialog.askopenfilename(
        title="Select a text file",             # Title of the file dialog
        initialdir="short_stories",             # Open directly to the "short_stories" folder
        filetypes=[("Text files", "*.txt")]     # Only show .txt files
    )
    return file_path             # Return the selected file's path

# Function to read and search the text
def readText(textfile, seek):
    with open(textfile, "rt") as f:       # Open the selected file
        lines = f.readlines()             # Read all lines into a list

    found = False                         # To check if the word is found at all
    total_count = 0                       # Counter for total occurrences
    print("----------------- Found on these lines -----------------")
    for i, line in enumerate(lines, 1):  # Enumerate lines, starting from line 1
        words = line.lower().split()     # Split the line into words
        line_count = words.count(seek)   # Count occurrences in the current line
        total_count += line_count        # Add to total occurrences

        if seek in words:                # If the word is found in the line
            found = True
            # Get the context of the word in the line
            for j, word in enumerate(words):
                if word == seek:
                    # Context adjustments
                    before = words[j-1] if j > 0 else ""  # Use an empty string if at the start
                    after = words[j+1] if j < len(words) - 1 else ""  # Use an empty string if at the end
                    context = f"... {before} {word} {after} ..." if before else f"... {word} {after} ..."
                    print(f"Line {i}: {context}")
    print("--------------------------------------------------------")
    # Print results
    if found:
        print(f"\nThe word '{seek}' was found {total_count} times in the document.")
    else:
        print(f"\nThe word '{seek}' was not found in the document.")
    print("--------------------------------------------------------")
    
# Main menu function
def srt():
    while True:
        print("----------------- Python Search Engine -----------------")
        print("| 1. Start                                             |")
        print("| 2. Exit                                              |")
        print("--------------------------------------------------------")
        print("Starting will open file explorer. Please select the .txt file you want the program to read.")
        choice = input("Enter your choice (1/2): ").strip()  # Get input and strip any whitespace

        if choice == "1":
            textfile = choose_file()         # Open file explorer
            if textfile:
                seek = input("What do you want to find? ").lower()
                readText(textfile, seek)     # Call the text search function
            break                            # Exit the menu loop after running the program
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break                            # Exit the menu loop to stop the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Run the program
srt()