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

    # Button for adding values to the table
    button = tk.Button(app_window, text="Add password", command=lambda: on_button_click(tree))
    button.pack(pady=10)

# Function for action after button is clicked, will add password
def on_button_click(tree):
    # Create a list that can hold the different values
    array_of_values = []

    # Create a pop-up window
    creation_window = tk.Tk()
    creation_window.title("Create new password-entry")
    creation_window.geometry("400x400")

    # Create the url input  
    url_label = tk.Label(creation_window, text="Enter the URL here:")
    url_label.pack()
    url = tk.Entry(creation_window)
    url.pack()
    print(url.get())
    array_of_values.append(url.get())
    

    # Create the username input
    username_label = tk.Label(creation_window, text="Enter the Username here:")
    username_label.pack()
    username = tk.Entry(creation_window)
    username.pack()
    array_of_values.append(username.get())

    # Create the password here:
    password_label = tk.Label(creation_window, text="Enter the Password here:")
    password_label.pack()
    password = tk.Entry(creation_window, show='•')
    password.pack()
    array_of_values.append(password.get())

    # add a submit button that closes the window and takes the values to the table
    submit_button = tk.Button(creation_window, text="Submit", command=lambda: append_to_table(array_of_values, tree, creation_window))
    submit_button.pack()

# Function for writing data to the table in the original window
def append_to_table(array_of_values, tree, popUp):
    popUp.destroy()

    print(array_of_values)
    for row in array_of_values:
        masked_password = "*" * len(row[2])
        tree.insert("", "end", values=(row[0], row[1], masked_password))
    
    
# Lets create and add the table to the window
create_table(app_window)



# Loop to start the application and keep it running
app_window.mainloop()