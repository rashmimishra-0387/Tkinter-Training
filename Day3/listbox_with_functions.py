import tkinter as tk

def insert_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def delete_item():
    selected_indices = listbox.curselection()
    # Delete from end to start to avoid index shift
    for index in selected_indices[::-1]:
        listbox.delete(index)

def get_items():
    items = listbox.get(0, tk.END)
    print("Items in Listbox:", items)

def clear_selection():
    listbox.selection_clear(0, tk.END)

root = tk.Tk()
root.title("Tkinter Listbox Management Example")

# Entry for inserting new items
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Button to insert item
insert_button = tk.Button(button_frame, text="Insert Item", command=insert_item)
insert_button.grid(row=0, column=0, padx=5)

# Button to delete selected item(s)
delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_item)
delete_button.grid(row=0, column=1, padx=5)

# Button to get all items
get_button = tk.Button(button_frame, text="Get Items", command=get_items)
get_button.grid(row=0, column=2, padx=5)

# Button to clear selection
clear_button = tk.Button(button_frame, text="Clear Selection", command=clear_selection)
clear_button.grid(row=0, column=3, padx=5)

# Listbox to display items
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
listbox.pack(padx=20, pady=20)

# Insert initial items
initial_items = ["Apple", "Banana", "Cherry", "Date"]
for item in initial_items:
    listbox.insert(tk.END, item)

root.mainloop()
