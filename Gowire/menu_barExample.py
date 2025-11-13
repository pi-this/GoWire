import tkinter as tk
from tkinter import Menu

def on_new_file():
    print("New File created!")

def on_open_file():
    print("File opened!")

def on_exit():
    root.quit()

root = tk.Tk()
root.title("Menu Example")

# Create a menu bar with a gray background
menu_bar = Menu(root, bg='gray', fg='black')

# Create a file menu
file_menu = Menu(menu_bar, tearoff=0, bg='lightblue', fg='black')  # Set background and foreground colors
file_menu.add_command(label="New", command=on_new_file)
file_menu.add_command(label="Open", command=on_open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)

# Add the file menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Start the main loop
root.mainloop()
