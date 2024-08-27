import tkinter as tk

def on_select(event):
    selected_indices = listbox.curselection()
    for index in selected_indices:
        print("Selected:", listbox.get(index))

win = tk.Tk()
win.title("Tkinter Listbox Example")

# Create a Listbox widget
#listbox = tk.Listbox(win)
listbox = tk.Listbox(win, selectmode=tk.MULTIPLE)
#listbox = tk.Listbox(win, exportselection=True)

listbox.pack(padx=20, pady=20)

# Insert items into the Listbox
for item in ["Apple", "Banana", "Cherry", "Date"]:
    listbox.insert(tk.END, item)

# Bind selection event
listbox.bind("<<ListboxSelect>>", on_select)

win.mainloop()
