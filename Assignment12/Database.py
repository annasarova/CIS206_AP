# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:05:50 2026

@author: Anna_Sarova
"""

import sqlite3

# ==============================
# DATABASE CONNECTION FUNCTION
# ==============================
def connect_db():
    """
    This function connects to the SQLite database file.
    If the database does not exist, it will be created.
    """
    return sqlite3.connect("northwind.db")


# ==============================
# GET TABLES FUNCTION
# ==============================
def get_tables(cursor):
    """
    This function retrieves all table names
    from the SQLite system table.
    """
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cursor.fetchall()


# ==============================
# GET COLUMN INFO FUNCTION
# ==============================
def get_columns(cursor, table):
    """
    This function retrieves column information
    for a given table using PRAGMA.
    """
    cursor.execute(f"PRAGMA table_info({table})")
    return cursor.fetchall()


# ==============================
# GET PRIMARY KEY FUNCTION
# ==============================
def get_primary_key(columns_info):
    """
    This function finds the primary key column
    (such as ProductID, CustomerID, etc.)
    """
    for col in columns_info:
        if col[5] == 1:  # Column marked as primary key
            return col[1]
    return None


# ==============================
# DISPLAY TABLE DATA FUNCTION
# ==============================
def display_table(cursor):
    """
    This function allows the user to select a table
    and displays all rows and column names.
    """

    # Get list of tables
    tables = get_tables(cursor)

    print("\nAvailable Tables:")
    for table in tables:
        print("-", table[0])

    table_name = input("\nEnter table name to view: ")

    try:
        # Execute SELECT query to read data
        cursor.execute(f"SELECT * FROM {table_name}")

        # Get column names
        column_names = [description[0] for description in cursor.description]
        print("\nColumns:", column_names)

        # Fetch all rows from table
        rows = cursor.fetchall()

        # Display rows with numbering
        print("\nData:")
        for i, row in enumerate(rows):
            print(f"{i+1}: {row}")

    except:
        print("Error: Invalid table name.")


# ==============================
# MODIFY DATA FUNCTION
# ==============================
def modify_data(cursor, conn):
    """
    This function allows the user to INSERT,
    UPDATE, or DELETE records from the database.

    Only the following tables are allowed:
    Customers, Employees, Products

    The program dynamically reads column names
    and uses the correct primary key.
    """

    allowed_tables = ["Customers", "Employees", "Products"]

    print("\nAllowed Tables:", allowed_tables)
    table = input("Enter table name: ")

    if table not in allowed_tables:
        print("Error: Table not allowed.")
        return

    # Get column information
    columns_info = get_columns(cursor, table)
    columns = [col[1] for col in columns_info]

    # Get primary key column
    pk = get_primary_key(columns_info)

    print("\nColumns:", columns)
    print("Primary Key:", pk)

    print("\n1. Insert")
    print("2. Update")
    print("3. Delete")

    choice = input("Choose an option: ")

    try:
        # ======================
        # INSERT DATA
        # ======================
        if choice == "1":
            values = []

            print("\nEnter values for each column (leave blank for ID):")

            for col in columns:
                val = input(f"{col}: ")

                # Allow primary key to auto-increment
                if col == pk and val == "":
                    values.append(None)
                else:
                    values.append(val)

            placeholders = ",".join(["?"] * len(columns))

            # Execute INSERT query
            cursor.execute(
                f"INSERT INTO {table} VALUES ({placeholders})",
                values
            )

            print("Record inserted successfully.")

        # ======================
        # UPDATE DATA
        # ======================
        elif choice == "2":
            record_id = input(f"Enter {pk} to update: ")

            print("\nSelect column to update:")
            for i, col in enumerate(columns):
                print(f"{i+1}. {col}")

            col_choice = int(input("Choose column number: "))
            column_name = columns[col_choice - 1]

            new_value = input(f"Enter new value for {column_name}: ")

            # Execute UPDATE query using correct primary key
            cursor.execute(
                f"UPDATE {table} SET {column_name}=? WHERE {pk}=?",
                (new_value, record_id)
            )

            print("Record updated successfully.")

        # ======================
        # DELETE DATA
        # ======================
        elif choice == "3":
            record_id = input(f"Enter {pk} to delete: ")

            # Execute DELETE query using correct primary key
            cursor.execute(
                f"DELETE FROM {table} WHERE {pk}=?",
                (record_id,)
            )

            print("Record deleted successfully.")

        else:
            print("Invalid choice.")

        # Save changes to database
        conn.commit()

    except Exception as e:
        print("Error:", e)


# ==============================
# MAIN MENU FUNCTION
# ==============================
def main():
    """
    This is the main function of the program.
    It displays a menu and allows the user
    to choose different database activities.
    """

    # Connect to database
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        print("\n===== DATABASE MENU =====")
        print("1. View Tables and Data (READ)")
        print("2. Modify Data (INSERT, UPDATE, DELETE)")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # Option 1: Read database
        if choice == "1":
            display_table(cursor)

        # Option 2: Modify database
        elif choice == "2":
            modify_data(cursor, conn)

        # Option 3: Exit program
        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")

    # Close database connection
    conn.close()


# ==============================
# PROGRAM START
# ==============================
# This starts the execution of the program
main()