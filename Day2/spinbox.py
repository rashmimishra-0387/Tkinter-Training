import tkinter as tk

win = tk.Tk()
win.title("Tkinter Spinbox Example")

def spinbox_changed():
    print("Value changed to:", spinbox.get())

# Create a Spinbox with values and custom format
spinbox = tk.Spinbox(win, values=('Apple', 'Banana', 'Cherry'))
spinbox.pack(pady=20)

# Create a Spinbox with floating point values and custom format
float_spinbox = tk.Spinbox(win, from_=0, to=10, increment=0.5, format='%04.1f')
float_spinbox.pack(pady=10)

# Create a Spinbox with floating point values and custom format
float_spinbox = tk.Spinbox(win, from_=0, to=10, increment=2)
float_spinbox.pack(pady=10)

#state: Controls the state of the Spinbox widget ('normal', 'disabled', or 'readonly').
spinbox = tk.Spinbox(win, from_=0, to=10, state='readonly')
spinbox.pack(pady=20)

#command: Specifies a function to call whenever the value in the Spinbox changes.

spinbox = tk.Spinbox(win, from_=0, to=10, command=spinbox_changed)
spinbox.pack(pady=20)

win.mainloop()
