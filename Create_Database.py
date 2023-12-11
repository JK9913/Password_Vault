import myDBconfig as myDB
from pprint import pprint
import mysql.connector as mysql
conn = mysql.connect(**myDB.dbConfig)
cursor = conn.cursor()
import os

# Creating some global variables about the path currently used
current_directory = os.getcwd()
print(current_directory)

# This function checks if the named database exists
def check_database(cursor, database_name):

    cursor.execute("SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = %s", (database_name,))
    result = cursor.fetchone()

    if result:
        print(f"Database '{database_name}' exists")
        return True
    else:
        print(f"Database '{database_name}' does not exist")
        return False


# This function creates a named database
def create_database(cursor, name_of_database):
    
    cursor.execute(f"CREATE DATABASE {name_of_database}")

    result = cursor.fetchall()
    print("result\nDatabase created.")


def create_table(cursor, name_of_database, name_of_table):
    # Uses the named database
    cursor.execute(f"USE {name_of_database}")

    # Getting the tables and checking if the table we want exists
    tables = cursor.fetchall()

    if not name_of_table in str(tables):
        #with open()
        # Write something about the with name in the project. It opens and makes sure everything is closed if something crashes.
        pass