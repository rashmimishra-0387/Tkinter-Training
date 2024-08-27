import tkinter as tk

root = tk.Tk()
root.title("Tkinter Frame Example")

# Create a frame
frame = tk.Frame(root, borderwidth=2, relief="ridge")
frame.pack(padx=20, pady=20, expand=True)

# Add widgets to the frame
label = tk.Label(frame, text="This is a label inside the frame")
label.pack(padx=10, pady=10)

button = tk.Button(frame, text="Click me!")
button.pack(padx=10, pady=10)

root.mainloop()
