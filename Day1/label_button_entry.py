import tkinter as tk

window = tk.Tk()
window.title("Basic Widgets - Label, Button and Entry")
window.geometry("400x300")
window.configure(bg="lightblue")


#Label
label1 = tk.Label(window, 
                  text="Hello, World!", 
                  font=("Helvetica", 16), 
                  fg="white", 
                  bg="black",
                  bd=2,     #Specifies the width of the label's border.
                  width=20, #Specifies the width of the label widget in characters.
                  height=3, #Specifies the height of the label widget in lines (text lines).
                  anchor=tk.CENTER,  #Specifies where the text should be positioned within the label. Values include tk.N, tk.S, tk.E, tk.W, tk.CENTER
                  justify=tk.CENTER, #Specifies how multiple lines of text should be aligned. Options are tk.LEFT, tk.RIGHT, and tk.CENTER
                  relief=tk.RAISED,  #Specifies the border decoration. Options include tk.FLAT, tk.SUNKEN, tk.RAISED, tk.GROOVE, and tk.RIDGE
                  padx=10, 
                  pady=5)
label1.pack()


#button 
button1 = tk.Button(window, 
                    text="Click Me!", 
                    command=window.destroy, 
                    font=("Arial", 12), 
                    fg="white", 
                    bg="purple", 
                    width=15, 
                    height=2,
                    state=tk.ACTIVE, # Specifies the state of the button. Options are tk.NORMAL, tk.DISABLED, and tk.ACTIVE.
                    relief=tk.RIDGE, 
                    padx=10, 
                    pady=5)
button1.pack()

#Input Box 
entry1 = tk.Entry(window, 
                  width=40, 
                  font=("Times", 14), 
                  fg="black", 
                  bg="white", 
                  justify=tk.LEFT, 
                  bd=3, 
                  relief=tk.SUNKEN)
val = entry1.get()

entry1.pack()

window.mainloop()