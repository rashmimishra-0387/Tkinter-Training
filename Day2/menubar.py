import tkinter as tk
from tkinter import Menu

def file_new():
    print("New File")

def file_open():
    print("Open File")

def file_save():
    print("Save File")

def help_about():
    print("About")

win = tk.Tk()
win.title("Tkinter Menubar Example")

# Create a menu bar
menubar = Menu(win)    # creating object of menubar will serve as the main menubar for the application.
win.config(menu=menubar) #associates the menubar with the main window

# Create File menu
file_menu = Menu(menubar, tearoff=1) # creates a dropdown menu (file_menu) under the "File" 
#tearoff=0: This optional parameter specifies whether the menu can be "torn off" and displayed as a separate window.Posible values = 0,1
menubar.add_cascade(label="File", menu=file_menu) # adds the "File" menu to the menubar(main menu items).
file_menu.add_command(label="New", command=file_new) #adds a command item "New" to the "File" menu that calls the file_new() function when clicked.
file_menu.add_command(label="Open", command=file_open) #adds a command item "open" to the "File" menu that calls the file_open() function when clicked.
file_menu.add_command(label="Save", command=file_save)#adds a command item "Save" to the "File" menu that calls the file_save() function when clicked.
file_menu.add_separator() # adds a separator line in the "File" menu.
file_menu.add_command(label="Exit", command=win.quit)

# Create Help menu
help_menu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=help_about)
win.mainloop()
