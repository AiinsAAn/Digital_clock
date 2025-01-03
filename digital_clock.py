import tkinter as tk
from time import strftime

# Function to update the time on the clock
def update_time():
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    clock_label.config(text=current_time)  # Update label with current time
    clock_label.after(1000, update_time)  # Update every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)  # Prevent resizing the window

# Style for the clock
clock_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 48, "bold"),
    fg="cyan",
    bg="black",
    pady=20
)
clock_label.pack(expand=True)

# Call the update_time function to start the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
