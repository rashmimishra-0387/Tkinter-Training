import tkinter as tk

def listbox_scroll(*args):
    listbox.yview(*args)

root = tk.Tk()
root.title("Listbox Scroll Example")

# Create a Listbox and populate with items
listbox = tk.Listbox(root, height=10)
for i in range(50):
    listbox.insert(tk.END, f"Item {i+1}")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar and associate it with the Listbox
scrollbar = tk.Scrollbar(root, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Example usage of listbox_scroll function
def scroll_up():
    listbox_scroll('scroll', -1, 'units')

def scroll_down():
    listbox_scroll('scroll', 1, 'units')

# Buttons to demonstrate scrolling
up_button = tk.Button(root, text="Scroll Up", command=scroll_up)
up_button.pack()

down_button = tk.Button(root, text="Scroll Down", command=scroll_down)
down_button.pack()

root.mainloop()
