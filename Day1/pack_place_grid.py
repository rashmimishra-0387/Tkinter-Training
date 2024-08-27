import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

#possible options for pack is - fill, expand, and side
label1 = tk.Label(root, text="Label 1", bg = "green")
label1.pack(fill = tk.Y, anchor = "e")

label2 = tk.Label(root, text="Label 2", bg = "red")
label2.pack(expand = True)

label3 = tk.Label(root, text="Label 3", bg = "red")
label3.pack(anchor="n")

"""
#grid options: - rowspan, columnspan, sticky, and padding 
label1 = tk.Label(root, text="Label 1", bg = "skyblue")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=1, column=0, sticky=tk.W)


label3 = tk.Label(root, text="Label 3", bg="pink")
label3.grid(row=3, column=0, ipadx=10, ipady=5)

label4 = tk.Label(root, text="Label 4", bg="pink")
label4.grid(row=3, column=1, padx=10, pady=5)


# place - x and y, relx and rely, width and height, anchor, bordermode
label1 = tk.Label(root, text="Label 1", bg = "red")
label1.place(x=10, y=20)

label2 = tk.Label(root, text="Label 2", bg = "blue")
label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label3 = tk.Label(root, text="Label 3", bg = "pink")
label3.place(x=100, y=20, width=100, height=30)

label4 = tk.Label(root, text="Label 4", bg = "skyblue")
label4.place(x=10, y=200, bordermode=tk.OUTSIDE)
"""

root.mainloop()
