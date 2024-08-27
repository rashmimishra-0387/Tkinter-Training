import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Information", "This is an informational message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

def show_error():
    messagebox.showerror("Error", "This is an error message.")

def ask_question():
    result = messagebox.askquestion("Question", "Do you want to proceed?")
    messagebox.showinfo("Response", f"Your response: {result}")

def ask_yes_no():
    result = messagebox.askyesno("Question", "Do you agree?")
    if result:
        messagebox.showinfo("Agreement", "You agreed.")
    else:
        messagebox.showwarning("Disagreement", "You did not agree.")

def ask_yes_no_cancel():
    result = messagebox.askyesnocancel("Question", "Do you want to save changes?")
    if result is True:
        messagebox.showinfo("Save", "Changes will be saved.")
    elif result is False:
        messagebox.showinfo("Discard", "Changes will not be saved.")
    else:
        messagebox.showinfo("Cancel", "Operation canceled.")

def ask_retry_cancel():
    result = messagebox.askretrycancel("Question", "Failed to connect. Retry?")
    if result:
        messagebox.showinfo("Retry", "Trying again...")
    else:
        messagebox.showwarning("Cancel", "Operation canceled.")

def ask_ok_cancel():
    result = messagebox.askokcancel("Question", "Do you want to proceed?")
    if result:
        messagebox.showinfo("Proceed", "Proceeding with operation.")
    else:
        messagebox.showwarning("Cancel", "Operation canceled.")

root = tk.Tk()
root.title("Tkinter Message Boxes Example")

# Buttons for each type of message box
info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack(pady=5, padx=10, fill=tk.X)

warning_button = tk.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=5, padx=10, fill=tk.X)

error_button = tk.Button(root, text="Show Error", command=show_error)
error_button.pack(pady=5, padx=10, fill=tk.X)

question_button = tk.Button(root, text="Ask Question", command=ask_question)
question_button.pack(pady=5, padx=10, fill=tk.X)

yes_no_button = tk.Button(root, text="Ask Yes/No", command=ask_yes_no)
yes_no_button.pack(pady=5, padx=10, fill=tk.X)

yes_no_cancel_button = tk.Button(root, text="Ask Yes/No/Cancel", command=ask_yes_no_cancel)
yes_no_cancel_button.pack(pady=5, padx=10, fill=tk.X)

retry_cancel_button = tk.Button(root, text="Ask Retry/Cancel", command=ask_retry_cancel)
retry_cancel_button.pack(pady=5, padx=10, fill=tk.X)

ok_cancel_button = tk.Button(root, text="Ask OK/Cancel", command=ask_ok_cancel)
ok_cancel_button.pack(pady=5, padx=10, fill=tk.X)

root.mainloop()
