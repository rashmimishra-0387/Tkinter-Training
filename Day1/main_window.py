import tkinter as tk

#This creates the main window object (root) using Tk() constructor.
window = tk.Tk()

#sets title
window.title("My Tkinter Window")

#initial size of the window. The format is "widthxheight"
window.geometry("400x300")

#setting the background color of the window.
window.configure(bg="lightblue")

#whether the window can be resized horizontally (width=True) and vertically (height=True).
window.resizable(width=True, height=True)

# Step 4: Displaying the Window
window.mainloop()