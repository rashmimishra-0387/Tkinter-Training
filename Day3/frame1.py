import tkinter as tk

win = tk.Tk()
win.title("Nested Frames Example")

# Main frame
main_frame = tk.Frame(win, borderwidth=3, relief="ridge")
#main_frame.pack(padx=50, pady=50)
#main_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
#main_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Frame 1 inside main frame
frame1 = tk.Frame(main_frame, borderwidth=2, relief="groove")
#frame1.pack(side=tk.LEFT, padx=20, pady=20)
frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
label1 = tk.Label(frame1, text="Frame 1")
label1.pack()

# Frame 2 inside main frame
frame2 = tk.Frame(main_frame, borderwidth=2, relief="groove")
frame2.pack(side=tk.RIGHT, padx=20, pady=20)

label2 = tk.Label(frame2, text="Frame 2")
label2.pack()

win.mainloop()
