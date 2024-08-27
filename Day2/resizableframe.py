import tkinter as tk

win = tk.Tk()
win.title("Nested Frames Example")

# Configure the main window to be resizable
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)

# Main frame
main_frame = tk.Frame(win, borderwidth=3, relief="ridge")
main_frame.grid(sticky="nsew", padx=50, pady=50)

# Configure the main frame to be resizable
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

# Frame 1
frame1 = tk.Frame(main_frame, borderwidth=2, relief="groove")
frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
label1 = tk.Label(frame1, text="Frame 1")
label1.pack()

# Frame 2 inside main frame
frame2 = tk.Frame(main_frame, borderwidth=2, relief="groove")
frame2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
label2 = tk.Label(frame2, text="Frame 2")
label2.pack()

win.mainloop()
