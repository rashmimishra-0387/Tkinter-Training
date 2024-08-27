import tkinter as tk
from tkinter import Menu

def hello():
    print("Hello!")

root = tk.Tk()
menubar = Menu(root)

# Create a tear-off menu
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
