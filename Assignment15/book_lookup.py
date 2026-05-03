# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:53:26 2026

@author: Anna Sarova
"""

"""
Program: Book Lookup (JSON & XML)
Description:
    This program loads book data from JSON and XML files,
    displays the contents, and allows the user to search
    for books by title repeatedly.
"""

import json
import xml.etree.ElementTree as ET


def load_json_file(filename):
    """
    Load book data from a JSON file.

    Parameters:
        filename (str): Path to JSON file

    Returns:
        list: List of book dictionaries
    """
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string.")

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get("books", [])
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def load_xml_file(filename):
    """
    Load book data from an XML file.

    Parameters:
        filename (str): Path to XML file

    Returns:
        list: List of book dictionaries
    """
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string.")

    books = []

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for book in root.findall("book"):
            books.append({
                "title": book.find("title").text,
                "author": book.find("author").text,
                "year": int(book.find("year").text),
                "available": book.find("available").text
            })

        return books

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except ET.ParseError:
        print("Error: Invalid XML format.")
        return []


def display_books(books):
    """
    Display all books.

    Parameters:
        books (list): List of book dictionaries
    """
    if not isinstance(books, list):
        raise ValueError("Books must be a list.")

    print("\nLibrary Contents:")
    print("-" * 40)

    for book in books:
        print(f"{book['title']} by {book['author']} ({book['year']})"
              f" - Available: {book['available']}")


def find_book(books, title):
    """
    Search for a book by title.

    Parameters:
        books (list): List of book dictionaries
        title (str): Title to search for

    Returns:
        dict or None: Found book or None
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")

    for book in books:
        if book["title"].lower() == title.lower():
            return book

    return None


def prompt_user_search(books):
    """
    Repeatedly prompt user for book titles and search.

    Parameters:
        books (list): List of book dictionaries
    """
    while True:
        title = input("\nEnter book title (or 'exit' to quit): ").strip()

        if title.lower() == "exit":
            print("Exiting search.")
            break

        if not title:
            print("Invalid input. Please enter a valid title.")
            continue

        result = find_book(books, title)

        if result:
            print(f"Found: {result['title']} by {result['author']} "
                  f"({result['year']}) - Available: {result['available']}")
        else:
            print(f"{title} - Title not found.")


def main():
    print("=== JSON Processing ===")
    json_books = load_json_file("books.json")
    display_books(json_books)
    prompt_user_search(json_books)

    print("\n=== XML Processing ===")
    xml_books = load_xml_file("books.xml")
    display_books(xml_books)
    prompt_user_search(xml_books)


main()
