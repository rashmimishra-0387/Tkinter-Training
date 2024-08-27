import tkinter as tk
from tkinter import messagebox

def submit_form():
    selected_color = color_var.get()
    selected_options = []
    
    if option1_var.get():
        selected_options.append("Option 1")
    if option2_var.get():
        selected_options.append("Option 2")
    if option3_var.get():
        selected_options.append("Option 3")
    
    message = f"Selected Color: {selected_color}\nSelected Options: {', '.join(selected_options)}"
    messagebox.showinfo("Form Submission", message)

# Create the main window
root = tk.Tk()
root.title("Tkinter Radio Button and Checkbox Example")

# Define variables for radio buttons and checkboxes
color_var = tk.StringVar(value="Red")
option1_var = tk.BooleanVar(value=False)
option2_var = tk.BooleanVar(value=False)
option3_var = tk.BooleanVar(value=False)

# Create and place radio buttons
tk.Label(root, text="Select a color:").pack()

color_frame = tk.Frame(root)
color_frame.pack()

tk.Radiobutton(color_frame, text="Red", variable=color_var, value="Red").pack(anchor='w')
tk.Radiobutton(color_frame, text="Green", variable=color_var, value="Green").pack(anchor='w')
tk.Radiobutton(color_frame, text="Blue", variable=color_var, value="Blue").pack(anchor='w')

# Create and place checkboxes
tk.Label(root, text="Select options:").pack()

option_frame = tk.Frame(root)
option_frame.pack()

tk.Checkbutton(option_frame, text="Option 1", variable=option1_var).pack(anchor='w')
tk.Checkbutton(option_frame, text="Option 2", variable=option2_var).pack(anchor='w')
tk.Checkbutton(option_frame, text="Option 3", variable=option3_var).pack(anchor='w')

# Create and place the submit button
tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

# Run the application
root.mainloop()
