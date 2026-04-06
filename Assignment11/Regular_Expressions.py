# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:16:40 2026

@author: Anna SAROVA
"""

import re

# -------------------------------
# 1. Alphanumeric String Check
# Description: Checks if a string contains only letters (a-z, A-Z) and numbers (0-9).
# -------------------------------
def problem_1():
    pattern = r'^[a-zA-Z0-9]+$'
    tests = ["ABCDEFabcdef123450", "*&%@#!}{"]
    print("1. Alphanumeric String Check")
    print("Description: Only allows letters and numbers.\n")
    for t in tests:
        print(t, "->", bool(re.match(pattern, t)))

# -------------------------------
# 2. 'a' followed by zero or more 'b'
# Description: Matches strings that start with 'a' and may have any number of 'b's after.
# -------------------------------
def problem_2():
    pattern = r'^ab*$'
    tests = ["ab", "abc", "a", "ab", "abb"]
    print("2. 'a' followed by zero or more 'b'")
    print("Description: Matches 'a', 'ab', 'abb', etc.\n")
    for t in tests:
        print(t, "->", bool(re.match(pattern, t)))

# -------------------------------
# 3. 'a' followed by one or more 'b'
# Description: Matches strings starting with 'a' and at least one 'b'.
# -------------------------------
def problem_3():
    pattern = r'^ab+$'
    tests = ["ab", "abc", "a", "ab", "abb"]
    print("3. 'a' followed by one or more 'b'")
    print("Description: Must contain at least one 'b' after 'a'.\n")
    for t in tests:
        print(t, "->", bool(re.match(pattern, t)))

# -------------------------------
# 4. Lowercase Words with Underscore
# Description: Matches lowercase words joined by a single underscore.
# -------------------------------
def problem_4():
    pattern = r'^[a-z]+_[a-z]+$'
    tests = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
    print("4. Lowercase Words Joined by Underscore")
    print("Description: Only lowercase letters allowed on both sides of '_'.\n")
    for t in tests:
        print(t, "->", bool(re.match(pattern, t)))

# -------------------------------
# 5. Word at Beginning of String
# Description: Finds a word at the start of a string.
# -------------------------------
def problem_5():
    pattern = r'^\w+'
    tests = [
        "The quick brown fox jumps over the lazy dog.",
        " The quick brown fox jumps over the lazy dog."
    ]
    print("5. Match Word at Beginning")
    print("Description: Returns first word if it starts immediately.\n")
    for t in tests:
        match = re.match(pattern, t)
        print(t, "->", match.group() if match else None)

# -------------------------------
# 6. Words Containing 'z'
# Description: Finds all words that contain the letter 'z'.
# -------------------------------
def problem_6():
    pattern = r'\b\w*z\w*\b'
    tests = [
        "The quick brown fox jumps over the lazy dog.",
        "Python Exercises."
    ]
    print("6. Words Containing 'z'")
    print("Description: Finds all words that include 'z'.\n")
    for t in tests:
        print(re.findall(pattern, t))

# -------------------------------
# 7. Remove Leading Zeros from IP
# Description: Removes unnecessary leading zeros from an IP address.
# -------------------------------
def problem_7():
    ip = "216.08.094.196"
    result = re.sub(r'\b0+(\d)', r'\1', ip)
    print("7. Remove Leading Zeros from IP")
    print("Description: Cleans up IP formatting.\n")
    print(result)

# -------------------------------
# 8. Search for Specific Words
# Description: Checks if given words exist in a string.
# -------------------------------
def problem_8():
    text = 'The quick brown fox jumps over the lazy dog.'
    words = ['fox', 'dog', 'horse']
    print("8. Search for Literal Strings")
    print("Description: Checks if specific words exist.\n")
    for word in words:
        print(word, "->", "Found" if re.search(word, text) else "Not Found")

# -------------------------------
# 9. Find Position of Word
# Description: Finds the starting index of a word in a string.
# -------------------------------
def problem_9():
    text = 'The quick brown fox jumps over the lazy dog.'
    word = 'fox'
    match = re.search(word, text)
    print("9. Find Word Position")
    print("Description: Returns index where word starts.\n")
    if match:
        print("Found at position", match.start())

# -------------------------------
# 10. Replace Spaces and Underscores
# Description: Converts spaces to underscores and vice versa.
# -------------------------------
def problem_10():
    def swap(s):
        return re.sub(r'_', ' ', s) if "_" in s else re.sub(r'\s', '_', s)
    print("10. Swap Spaces and Underscores")
    print("Description: Converts between spaces and underscores.\n")
    print(swap("Regular Expressions"))
    print(swap("Code_Examples"))

# -------------------------------
# 11. Extract Date from URL
# Description: Extracts year, month, and day from a URL.
# -------------------------------
def problem_11():
    url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/example/"
    pattern = r'/(\d{4})/(\d{2})/(\d{2})/'
    match = re.search(pattern, url)
    print("11. Extract Date from URL")
    print("Description: Pulls year, month, and day.\n")
    if match:
        print("Year:", match.group(1))
        print("Month:", match.group(2))
        print("Day:", match.group(3))

# -------------------------------
# 12. Words Starting with 'a' or 'e'
# Description: Finds words beginning with 'a' or 'e'.
# -------------------------------
def problem_12():
    text = "The following example creates an ArrayList with a capacity of 50 elements."
    pattern = r'\b[aeAE]\w*'
    print("12. Words Starting with 'a' or 'e'")
    print("Description: Finds all matching words.\n")
    print(re.findall(pattern, text))

# -------------------------------
# 13. Replace Punctuation with Colon
# Description: Replaces spaces, commas, and dots with colons.
# -------------------------------
def problem_13():
    text = 'Python Exercises, PHP exercises.'
    result = re.sub(r'[ ,.]', ':', text)
    print("13. Replace Space/Comma/Dot with Colon")
    print("Description: Normalizes separators.\n")
    print(result)

# -------------------------------
# 14. Words Starting with 'a' or 'e'
# Description: Same as Problem 12.
# -------------------------------
def problem_14():
    text = "The following example creates an ArrayList with a capacity of 50 elements."
    pattern = r'\b[aeAE]\w*'
    print("14. Words Starting with 'a' or 'e'")
    print("Description: Same as problem 12.\n")
    print(re.findall(pattern, text))

# -------------------------------
# 15. Remove Extra Spaces
# Description: Replaces multiple spaces with a single space.
# -------------------------------
def problem_15():
    text = 'Python      Exercises'
    result = re.sub(r'\s+', ' ', text)
    print("15. Remove Multiple Spaces")
    print("Description: Cleans up spacing.\n")
    print(result)


# -------------------------------
# Main Runner
# -------------------------------
def main():
    problem_1()
    print()
    problem_2()
    print()
    problem_3()
    print()
    problem_4()
    print()
    problem_5()
    print()
    problem_6() 
    print()
    problem_7() 
    print()
    problem_8() 
    print()
    problem_9() 
    print()
    problem_10() 
    print()
    problem_11() 
    print()
    problem_12() 
    print()
    problem_13() 
    print()
    problem_14() 
    print()
    problem_15()

main()

