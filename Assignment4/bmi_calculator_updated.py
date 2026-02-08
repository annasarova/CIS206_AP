# -*- coding: utf-8 -*-
"""
Created on Sat Feb 7 21:09:20 2026

@author: Anna Sarova
"""

"""
BMI Calculator (Imperial Units)

Enhanced for Session 4:
- Data validation
- Exception handling
- Nested conditions
"""

def calculate_bmi(weight_lbs, height_inches):
    """
    Calculate BMI using imperial-to-metric conversion.

    Parameters:
        weight_lbs (float): Weight in pounds
        height_inches (float): Height in inches

    Returns:
        float: Calculated BMI
    """
    # Convert pounds to kilograms
    weight_kg = weight_lbs * 0.453592

    # Convert inches to meters
    height_m = height_inches * 0.0254

    # ---------------------------------------------------
    # REQUIREMENT 2: EXCEPTION HANDLING (division safety)
    # ---------------------------------------------------
    if height_m == 0:
        raise ZeroDivisionError("Height cannot be zero.")

    return weight_kg / (height_m ** 2)


def determine_bmi_category(bmi):
    """
    Determine BMI category using standard ranges.
    """

    # ----------------------------------
    # REQUIREMENT 3: NESTED IF STATEMENT
    # ----------------------------------
    if bmi < 18.5:
        if bmi < 16:
            return "Severely Underweight"
        else:
            return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    else:
        return "Overweight"


def main():
    """
    Main program execution with validation and exception handling.
    """

    try:
        # -----------------------------------
        # REQUIREMENT 1: DATA TYPE VALIDATION
        # -----------------------------------
        weight_lbs = float(input("Enter your weight in pounds: "))
        height_feet = int(input("Enter your height (feet): "))
        height_inches = int(input("Enter remaining height (inches): "))

        # ---------------------------------
        # REQUIREMENT 1: RANGE VALIDATION
        # ---------------------------------
        if weight_lbs <= 0:
            raise ValueError("Weight must be greater than zero.")

        if height_feet < 0 or height_inches < 0:
            raise ValueError("Height values cannot be negative.")

        # Convert total height to inches
        total_height_inches = (height_feet * 12) + height_inches

        if total_height_inches <= 0:
            raise ValueError("Total height must be greater than zero.")

        bmi = calculate_bmi(weight_lbs, total_height_inches)
        bmi_category = determine_bmi_category(bmi)

        # Output formatted to one decimal place
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Category: {bmi_category}")

        # BMI legend
        print("\nBMI Categories (Source: Wikipedia - Body Mass Index):")
        print("Severely Underweight: BMI < 16")
        print("Underweight: BMI 16 – 18.4")
        print("Normal weight: BMI 18.5 – 24.9")
        print("Overweight: BMI 25.0 and above")

    # ---------------------------------
    # REQUIREMENT 2: EXCEPTION HANDLING
    # ---------------------------------
    except ValueError as ve:
        print("\nINPUT ERROR:", ve)

    except ZeroDivisionError as zde:
        print("\nMATH ERROR:", zde)

    except Exception as e:
        print("\nUNEXPECTED ERROR:", e)

    finally:
        print("\nProgram execution completed.")


main()
