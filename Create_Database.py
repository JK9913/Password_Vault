import myDBconfig as myDB
from pprint import pprint
import mysql.connector as mysql
conn = mysql.connect(**myDB.dbConfig)
cursor = conn.cursor()
import os

# Creating some global variables about the path currently used
current_directory = os.getcwd()
sql_File = current_directory + r"\Password_Vault_Table.sql"


# This function checks if the named database exists
def check_database(database_name):

    cursor.execute("SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = %s", (database_name,))
    result = cursor.fetchone()

    if result:
        print(f"Database '{database_name}' exists")
        return True
    else:
        print(f"Database '{database_name}' does not exist")
        return False


# This function creates a named database
def create_database(name_of_database):
    
    cursor.execute(f"CREATE DATABASE {name_of_database}")

    result = cursor.fetchall()
    print(f"{result}\nDatabase created.")


def create_table(name_of_database, name_of_table):
    # Uses the named database
    cursor.execute(f"USE {name_of_database}")

    # Getting the tables and checking if the table we want exists
    cursor.execute(f"SHOW TABLES")
    tables = cursor.fetchall()

    if not name_of_table in str(tables):
        with open(sql_File, "r") as file_to_read:
            sql_script = file_to_read.read()
        # Write something about the with name in the project. It opens and makes sure everything is closed if something crashes.
        
        print("running script to create tables")
        cursor.execute(sql_script)
    else:
        print("table exists, no need to create.")

def get_data(name_of_database):
    # Use the named database
    try:
        cursor.execute(f"USE {name_of_database}")
    except:
        print(f"Already using {name_of_database}")

    # Run query to fetch data
    try:
        cursor.execute(f"SELECT websiteURL, username, password_cipher FROM userVault")
        pprint(cursor.fetchall())
        return cursor.fetchall()
    except mysql.Error as err:
        print(f"No result in the search: {err}")

def check_master_password(name_of_database):
    try:
        cursor.execute(f"USE {name_of_database}")
    except:
        print(f"Already using {name_of_database}")

    # Getting the tables and checking if the table we want exists
    cursor.execute(f"SHOW TABLES")
    tables = cursor.fetchall()

    if not "masterPassword" in str(tables): 
        # Create the table for the master password
        cursor.execute(f"CREATE TABLE IF NOT EXISTS masterPassword(id INT AUTO_INCREMENT PRIMARY KEY,password_hash VARCHAR(128) NOT NULL);")

        return False
    else:
        print("Table exists")
        return True

def write_master_password(password):
    pass