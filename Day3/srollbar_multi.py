import tkinter as tk

#*args  - allows the function to accept a variable number of arguments.
def listbox_scroll(*args):
    listbox.yview(*args)

def text_scroll(*args):
    text.yview(*args)

root = tk.Tk()
root.title("Tkinter Multiple Scrollbars Example")

# Frame for Listbox and its Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(side=tk.LEFT, fill=tk.Y)
#list_frame.pack(side=tk.LEFT)

#listbox = tk.Listbox(list_frame, width=30, height=10)
listbox = tk.Listbox(list_frame)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_list = tk.Scrollbar(list_frame, command=listbox.yview)
scrollbar_list.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar_list.set) # associates the Scrollbar with the Listbox for vertical scrolling.

# Inserting items into Listbox
for i in range(200):
    listbox.insert(tk.END, f"Item {i+1}")

# Frame for Text and its Scrollbar
text_frame = tk.Frame(root)
text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) # change to True

text = tk.Text(text_frame, width=40, height=4)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_text = tk.Scrollbar(text_frame, command=text.yview)
scrollbar_text.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scrollbar_text.set) #associates the Scrollbar with the Text widget for vertical scrolling.

# Inserting text into Text widget
sample_text = """
This widget provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox, Text and Canvas. Note that you can also create horizontal scrollbars on Entry widgets.
This widget provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox, Text and Canvas. Note that you can also create horizontal scrollbars on Entry widgets.
This widget provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox, Text and Canvas. Note that you can also create horizontal scrollbars on Entry widgets.
This widget provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox, Text and Canvas. Note that you can also create horizontal scrollbars on Entry widgets.
"""
text.insert(tk.END, sample_text)

root.mainloop()
