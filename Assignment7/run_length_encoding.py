# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 13:37:58 2026

@author: Anna Sarova
"""

"""
Run-Length Encoding Assignment
Author: Anna Sarova
Description:
This program demonstrates string manipulation and run-length encoding (RLE).
It includes:
- Activity 1: Basic string manipulation
- Activity 2: Run-length encoding function
- Activity 3: Run-length decoding and user input
"""


# ==========================================================
# Activity 1: String Manipulation Practice
# ==========================================================

def string_manipulation_demo():
    """
    Demonstrates basic string operations:
    length, indexing, slicing, and string methods.
    """
    text = "AAABBCDDDD"

    print("----- Activity 1: String Manipulation -----")
    print("Original String:", text)
    print("Length of string:", len(text))
    print("First character:", text[0])
    print("First three characters (slice):", text[0:3])
    print("Lowercase:", text.lower())
    print("Replaced A with Z:", text.replace("A", "Z"))
    print()


# ==========================================================
# Activity 2: Run-Length Encoding Function
# ==========================================================

def run_length_encode(input_string):
    """
    Encodes a string using run-length encoding (RLE).
    Example:
    AAABBCDDDD -> 3A2B1C4D
    """

    if not input_string:
        return ""

    encoded = ""
    count = 1

    # Loop through string starting from second character
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded += str(count) + input_string[i - 1]
            count = 1

    # Add the final character group
    encoded += str(count) + input_string[-1]

    return encoded


# ==========================================================
# Activity 3: Run-Length Decoding + User Input
# ==========================================================

def run_length_decode(encoded_string):
    """
    Decodes a run-length encoded string.
    Example:
    3A2B1C4D -> AAABBCDDDD
    """

    decoded = ""
    count = ""

    for char in encoded_string:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count)
            count = ""

    return decoded


# ==========================================================
# Main Program
# ==========================================================

def main():
    """
    Main function to run all activities.
    """

    # Run Activity 1
    string_manipulation_demo()

    # Run Activity 2 (Encoding Example)
    print("----- Activity 2: Run-Length Encoding -----")
    sample_text = "AAABBCDDDD"
    encoded_text = run_length_encode(sample_text)
    print("Original:", sample_text)
    print("Encoded :", encoded_text)
    print()

    # Run Activity 3 (User Input + Decoding)
    print("----- Activity 3: User Input & Decoding -----")
    user_input = input("Enter a string to encode: ")
    encoded_output = run_length_encode(user_input)
    print("Encoded result:", encoded_output)

    decoded_output = run_length_decode(encoded_output)
    print("Decoded back:", decoded_output)


# This ensures main() runs only if file is executed directly
if __name__ == "__main__":
    main()

