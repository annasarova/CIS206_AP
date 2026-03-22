# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:58:36 2026

@author: Anna Sarova
"""

import csv

"""
Program: Northwind Customer Search
Description:
Reads the Northwind Customers file and stores customer data in a list of 
dictionaries.
Provides a menu interface to display or search customers by company name
or contact name.
"""

def load_customers(filename):
    """
    Reads the customer file and returns a list of customer dictionaries.
    Each dictionary contains company, contact and phone.
    """

    customers = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # skip header row

            for row in reader:
                customer = {
                    "company": row[1],
                    "contact": row[2],
                    "phone": row[9]
                }
                customers.append(customer)

    except FileNotFoundError:
        print("Error: File not found.")

    return customers

def display_customers(customers, field):
    """
    Displays all customers sorted by a selected field.
    field: "company" or "contact"
    """
    sorted_list = sorted(customers, key=lambda c: c[field].lower())

    for customer in sorted_list:
        if field == "company":
            print(f"Company: {customer['company']} | "
                  f"Contact: {customer['contact']} | "
                  f"Phone: {customer['phone']}")
        else:
            print(f"Contact: {customer['contact']} | "
                  f"Company: {customer['company']} | "
                  f"Phone: {customer['phone']}")

def search_customers(customers, field, search_text):
    """
    Searches customers by company or contact name.
    Returns a list of matching customers.
    """

    results = []

    for customer in customers:
        if search_text.lower() in customer[field].lower():
            results.append(customer)

    return results

def display_search_results(results):
    """
    Displays matching customer records with labeled fields.
    """

    if len(results) == 0:
        print("No matching records found.")
        return

    for customer in results:
        print("Company Name:", customer["company"])
        print("Contact Name:", customer["contact"])
        print("Phone Number:", customer["phone"])
        print()

def show_menu():
    """Displays the program menu."""

    print()
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")

def get_menu_choice():
    """
    Gets and validates the user's menu selection.
    Returns a valid choice between 1 and 5.
    """

    choice = input("Enter choice (1-5): ")

    while not choice.isdigit() or int(choice) < 1 or int(choice) > 5:
        print("Invalid choice. Please enter a number from 1 to 5.")
        choice = input("Enter choice (1-5): ")

    return int(choice)

def main():

    customers = load_customers("Northwind Customers.txt")

    running = True

    while running:

        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            display_customers(customers, "company")

        elif choice == 2:
            display_customers(customers, "contact")

        elif choice == 3:
            text = input("Enter company name or part of name: ").strip()

            if text == "":
                print("Search text cannot be empty.")
            else:
                results = search_customers(customers, "company", text)
                display_search_results(results)

        elif choice == 4:
            text = input("Enter contact name or part of name: ").strip()

            if text == "":
                print("Search text cannot be empty.")
            else:
                results = search_customers(customers, "contact", text)
                display_search_results(results)

        elif choice == 5:
            print("Exiting program.")
            running = False

main()
