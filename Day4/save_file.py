#creating sav file widjet

from tkinter import *
from tkinter.ttk import * 
from tkinter.filedialog import asksaveasfile

window = Tk()
window.geometry("100x50")
window.title("Saving a file")

def save():
    files = [("All Files", "*.*"), ("Python Files", "*.py"), ("Text Document", "*.txt")]
    file = asksaveasfile(filetypes = files, defaultextension = files)
   
button = Button(window, text = "Save file", command = lambda:save()).pack()

window.mainloop()