import tkinter as tk
import webbrowser
import time
import subprocess  # Import subprocess module

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

# Function to toggle fullscreen mode
def toggle_fullscreen():
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)

# Function to change screen size
def change_screen_size(size):
    root.geometry(size)

# Function to open the external video player
def open_video_player():
    subprocess.Popen(["python", "video_player.py"], shell=True)

# Create the main window
root = tk.Tk()
root.title("App Launcher")
root.configure(bg='blue')  # Set the default background color to blue

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu with an "Exit" option
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Create a "Settings" menu with screen size options
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Small Screen", command=lambda: change_screen_size("800x600"))
settings_menu.add_command(label="Medium Screen", command=lambda: change_screen_size("1024x768"))
settings_menu.add_command(label="Large Screen", command=lambda: change_screen_size("1280x1024"))

# Create 6 buttons for different apps and websites
buttons = [
    ("Google", "https://www.google.com"),
    ("YouTube", "https://www.youtube.com"),
    ("Facebook", "https://www.facebook.com"),
    ("Twitter", "https://www.twitter.com"),
    ("Instagram", "https://www.instagram.com"),
    ("GitHub", "https://www.github.com")
]

# Create a 2x3 grid for the buttons
for i, (btn_text, url) in enumerate(buttons):
    row, col = divmod(i, 3)
    tk.Button(root, text=btn_text, command=lambda u=url: open_website(u)).grid(row=row+1, column=col, padx=10, pady=10)

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

# Create a button to toggle fullscreen
fullscreen_button = tk.Button(root, text="Toggle Fullscreen", command=toggle_fullscreen)
fullscreen_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Create a button to start the external video player
video_player_button = tk.Button(root, text="Open Video Player", command=open_video_player)
video_player_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Start the clock update
update_clock()

# Run the GUI
root.mainloop()
