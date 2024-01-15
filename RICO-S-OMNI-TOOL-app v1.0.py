import tkinter as tk
import webbrowser
import time

# Function to open a website when a button is clicked
def open_website(url):
    webbrowser.open_new(url)

# Function to change the GUI background color
def change_color():
    color = color_entry.get()
    root.configure(bg=color)

# Function to update the clock
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)  # Update every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("App Launcher")

# Create 9 buttons for different apps and websites
buttons = [
    ("Google", "https://www.google.com"),
    ("YouTube", "https://www.youtube.com"),
    ("Facebook", "https://www.facebook.com"),
    ("Twitter", "https://www.twitter.com"),
    ("Instagram", "https://www.instagram.com"),
    ("GitHub", "https://www.github.com"),
    ("Wikipedia", "https://www.wikipedia.org"),
    ("LinkedIn", "https://www.linkedin.com"),
    ("Reddit", "https://www.reddit.com")
]

# Create a 3x3 grid for the buttons
for i, (btn_text, url) in enumerate(buttons):
    row, col = divmod(i, 3)
    tk.Button(root, text=btn_text, command=lambda u=url: open_website(u)).grid(row=row, column=col, padx=10, pady=10)

# Create an input field and button to change GUI background color
color_label = tk.Label(root, text="Enter Color:")
color_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
color_entry = tk.Entry(root)
color_entry.grid(row=3, column=2, padx=10, pady=10)
color_button = tk.Button(root, text="Change Color", command=change_color)
color_button.grid(row=3, column=3, padx=10, pady=10)

# Create a label for the clock
clock_label = tk.Label(root, text="", font=("Helvetica", 18))
clock_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

# Start the clock update
update_clock()

# Run the GUI
root.mainloop()
