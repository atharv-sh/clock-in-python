import tkinter as tk
from time import strftime

# Function to update the clock
def update_time():
    current_time = strftime('%H:%M:%S')  # Get the current time in HH:MM:SS format
    clock_label.config(text=current_time)  # Update the label with the current time
    clock_label.after(1000, update_time)  # Schedule the function to run again after 1 second

# Create the main window
root = tk.Tk()
root.title("Live Clock")
root.geometry("500x200")  # Set the size of the window

# Configure the layout
root.resizable(False, False)  # Disable resizing of the window
root.configure(bg="black")  # Set background color

# Create a label to display the time
clock_label = tk.Label(root, font=("Times New Roman", 50), fg="cyan", bg="black")
clock_label.pack(anchor="center", expand=True)  # Center the label in the window

# Start the clock
update_time()

# Run the application
root.mainloop()
