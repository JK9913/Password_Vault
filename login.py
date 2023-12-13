import tkinter as tk
import Password_Encryption as Encryption
import Create_Database as db


def login_window():
    # This is where the main window is created
    app_login_window = tk.Tk()

    # Title of the window
    app_login_window.title("Login")

    # Setting the size of the window
    app_login_window.geometry("400x400")


    master_password_exists = db.check_master_password("passwordVault")


    if not master_password_exists:
        # Create the master password input  
        password_label = tk.Label(app_login_window, text="Please enter you desired master password.\nThis password will unlock all passwords so choose carefully")
        password_label.pack()
        password = tk.Entry(app_login_window, show='•')
        password.pack()
        
        

        def get_text():
            password_to_be_hashed = password.get()
            # Encrypt the password
            hashed_password = Encryption.hash_password(password_to_be_hashed)

            # Write the hashed password to database
            db.write_master_password(hashed_password)

            # Close the window
            app_login_window.destroy()
            
        # add a submit button that closes the window and takes the value to the database
        submit_button = tk.Button(app_login_window, text="Submit", command=lambda: get_text())
        submit_button.pack()
        app_login_window.mainloop()
    
    else:
        # Create the master password input  
        password_label = tk.Label(app_login_window, text="Please enter your password:")
        password_label.pack()
        password = tk.Entry(app_login_window, show='•')
        password.pack()

        def check_password():
            password_to_be_checked = password.get()

            # Hash and check against the database
            hashed_password = Encryption.hash_password(password_to_be_checked)

            hashed_password_from_database = db.get_master_password()
           
            if hashed_password != hashed_password_from_database[0][0]:
                password_label.config(text="Wrong password, please try again")
            else:
                app_login_window.destroy()
                
        

        # add a submit button that closes the window and takes the value to the database
        submit_button = tk.Button(app_login_window, text="Submit", command=lambda: check_password())
        submit_button.pack()
        # app_login_window.mainloop()
        app_login_window.wait_window(app_login_window)
    
    return True