import tkinter as tk

def display_text():
    entered_text = entry.get()  # Retrieve text from Entry widget
    label.config(text=f"You entered: {entered_text}")  # Update Label text

root = tk.Tk()
root.title("Entry Widget Example")

# Create Entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)  # Add padding around the Entry widget

# Create Button widget
button = tk.Button(root, text="Display Text", command=display_text)
button.pack(pady=10)  # Add padding around the Button widget

# Create Label widget for displaying entered text
label = tk.Label(root, text="")
label.pack(pady=10)  # Add padding around the Label widget

root.mainloop()