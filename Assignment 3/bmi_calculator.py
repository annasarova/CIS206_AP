# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 21:09:20 2026

@author: Anna Sarova
"""

"""
BMI Calculator (Imperial Units)

This program calculates Body Mass Index (BMI) using weight in pounds
and height in feet and inches.

Coding standards used:
- PEP 8 for variable and function naming
- PEP 257 for function documentation
"""

def calculate_bmi(weight_lbs, height_inches):
    """
    Calculate BMI using imperial-to-metric conversion.

    Standards applied:
    - Function name uses lower_case_with_underscores (PEP 8)
    - Descriptive parameter names (PEP 8)
    - Docstring documents purpose, parameters, and return (PEP 257)

    Parameters:
        weight_lbs (float): Weight in pounds
        height_inches (float): Height in inches

    Returns:
        float: Calculated BMI
    """
    # Convert pounds to kilograms (MathIsFun conversion chart)
    weight_kg = weight_lbs * 0.453592

    # Convert inches to meters (MathIsFun conversion chart)
    height_m = height_inches * 0.0254

    return weight_kg / (height_m ** 2)


def determine_bmi_category(bmi):
    """
    Determine BMI category based on standard ranges.

    BMI ranges sourced from:
    Wikipedia - Body Mass Index
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    else:
        return "Overweight"


def main():
    """
    Main program execution.

    Standards applied:
    - Clear function separation
    - Descriptive variable names
    - User-friendly input/output
    """

    # Variable names use lower_case_with_underscores and 
    # describe stored values (PEP 8)
    weight_lbs = float(input("Enter your weight in pounds: "))
    height_feet = int(input("Enter your height (feet): "))
    height_inches = int(input("Enter remaining height (inches): "))

    # Convert total height to inches
    total_height_inches = (height_feet * 12) + height_inches

    bmi = calculate_bmi(weight_lbs, total_height_inches)
    bmi_category = determine_bmi_category(bmi)

    # Output formatted to one decimal place
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"Category: {bmi_category}")

    # BMI legend with source citation
    print("\nBMI Categories (Source: Wikipedia - Body Mass Index):")
    print("Underweight: BMI < 18.5")
    print("Normal weight: BMI 18.5 – 24.9")
    print("Overweight: BMI 25.0 and above")


main()
