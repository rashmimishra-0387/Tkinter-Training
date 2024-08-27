import tkinter as tk
from tkinter import ttk

def start_progress():
    progress_bar.start() # Start the animation

def stop_progress():
    progress_bar.stop()

win = tk.Tk()
win.title("Tkinter ProgressBar Example")

# Create a progressbar widget
# mode options - indeterminate" mode, the progress bar shows an animated, continuous loop that indicates the application is busy, but without showing specific progress. 
# This mode is typically used when the actual progress cannot be accurately determined.
"""
progress_bar = ttk.Progressbar(win, orient="horizontal", length=300, mode="determinate") 
progress_bar.pack(pady=20)


progress_bar = ttk.Progressbar(win, mode="determinate")
progress_bar['value'] = 50  # Set progress to 50%
progress_bar.pack(pady=20)
"""

progress_bar = ttk.Progressbar(win, orient="vertical",mode="indeterminate")
progress_bar.start()  # Start the animation
progress_bar.pack(pady=20)


# Create buttons to control the progress bar
start_button = tk.Button(win, text="Start Progress", command=start_progress)
start_button.pack(pady=10)

stop_button = tk.Button(win, text="Stop Progress", command=stop_progress)
stop_button.pack(pady=10)

win.mainloop()
