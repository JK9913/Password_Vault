import tkinter as tk
from tkinter import ttk

# This is where the main window is created
app_window = tk.Tk()

# Title of the window
app_window.title("My Password Vault")

# Setting the size of the window
app_window.geometry("800x800")

# Add content here

# Function for creating the mainview table
def create_table(window):
    # This is called a treeview
    tree = ttk.Treeview(window, columns=("URL", "Username", "Password"))

    # Setting the header names
    tree.heading("URL", text="URL")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")

    # Since there is an empty column first, we remove this
    tree.column("#0", width=0, stretch=tk.NO)

    # SAMPLE DATA
    data = [
        ("https://www.VG.no", "Test_User1", "pass123")
    ]

    for row in data:
        masked_password = "*" * len(row[2])
        tree.insert("", "end", values=(row[0], row[1], masked_password))

    
    # Center table
    tree.pack(expand=True, fill="both", pady=(20), padx=20)

# Function for action after button is clicked, will add password
def on_button_click():
    print("Testing")


# Lets create and add the table to the window
create_table(app_window)

# Button for adding values to the table
button = tk.Button(app_window, text="Add password", command=on_button_click)
button.pack(pady=10)

# Loop to start the application and keep it running
app_window.mainloop()