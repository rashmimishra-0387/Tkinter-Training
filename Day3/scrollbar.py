
import tkinter as tk

win = tk.Tk()
win.title("Tkinter Scrollbar Example")

# Create a Listbox widget
#listbox = tk.Listbox(win, width=40, height=12)
listbox = tk.Listbox(win)
listbox.pack(padx=20, pady=20)

# Create a Scrollbar widget
scrollbar = tk.Scrollbar(win, orient=tk.VERTICAL)
#scrollbar = tk.Scrollbar(win, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure Listbox to use Scrollbar
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

# Insert some items into the Listbox
for i in range(100):
    listbox.insert(tk.END, f"Item {i+1}")

win.mainloop()

"""

from tkinter import *
  
root = Tk() 
root.geometry("150x200") 
   
w = Label(root, text ='This is a sample text', 
          font = "50")  
  
w.pack() 
   
scroll_bar = Scrollbar(root) 
  
scroll_bar.pack( side = RIGHT, 
                fill = Y ) 
   
mylist = Listbox(root,  
                 yscrollcommand = scroll_bar.set ) 
   
for line in range(1, 100): 
    mylist.insert(END, "Item " + str(line)) 
  
mylist.pack( side = LEFT, fill = BOTH ) 
  
scroll_bar.config( command = mylist.yview )  #associates the Scrollbar with the Text widget for vertical scrolling.
   
root.mainloop() 
"""