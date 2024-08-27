import tkinter
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar")
        self.root.geometry("300x200")
        self.root.config(background="white")
        
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tkinter.Label(self.root, text="CALENDAR", bg="dark gray", font=("times", 24, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Year Label
        year_label = tkinter.Label(self.root, text="Enter Year", bg="light green")
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        # Year Entry
        self.year_entry = tkinter.Entry(self.root)
        self.year_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Show Calendar Button
        show_button = tkinter.Button(self.root, text="Show Calendar", fg="Black", bg="Red", command=self.show_calendar)
        show_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Exit Button
        exit_button = tkinter.Button(self.root, text="Exit", fg="Black", bg="Red", command=self.root.quit)
        exit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def show_calendar(self):
        # Create a new window to display the calendar
        cal_window = tkinter.Toplevel(self.root)
        cal_window.title("Yearly Calendar")
        cal_window.geometry("600x400")
        
        # Get the year from the entry
        try:
            year = int(self.year_entry.get())
        except ValueError:
            # Show an error message if the input is not a valid year
            error_label = tkinter.Label(cal_window, text="Invalid year entered!", fg="red")
            error_label.pack(pady=10)
            return
        
        # Generate the calendar content
        cal_content = calendar.calendar(year)
        
        # Create a Text widget for displaying the calendar
        cal_text = tkinter.Text(cal_window, wrap="none", font=("Consolas", 10, 'bold'))
        cal_text.insert(tkinter.END, cal_content)
        cal_text.pack(expand=True, fill='both')

        # Add a Scrollbar
        scrollbar = tkinter.Scrollbar(cal_window, command=cal_text.yview)
        scrollbar.pack(side='right', fill='y')
        cal_text.config(yscrollcommand=scrollbar.set)

if __name__ == "__main__":
    root = tkinter.Tk()
    app = CalendarApp(root)
    root.mainloop()
