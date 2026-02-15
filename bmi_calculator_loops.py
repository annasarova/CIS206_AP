# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 21:09:20 2026

@author: Anna Sarova
"""

"""
BMI Calculator (Imperial Units) - Enhanced with Loops

Activities Implemented:
1. Invalid input does not terminate program; user can retry or quit.
2. Main loop continues asking for BMI calculations until user exits.
3. Updated program and function documentation (Python docstring standard).
4. BMI table generation for heights 58–76 inches (step 2)
   and weights 100–250 pounds (step 10).
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


    # Exeption handling (division safety)
    if height_m == 0:
        raise ZeroDivisionError("Height cannot be zero.")

    return weight_kg / (height_m ** 2)


def determine_bmi_category(bmi):
    """
    Determine BMI category using standard ranges.
    
    Parameters:
        bmi (float): Calculated BMI

    Returns:
        str: BMI category description
    """
    
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
    
    print("Welcome to the BMI Calculator!\n")

    #-------------------------------------    
    # Activity 2: Sentinel-controlled loop
    #-------------------------------------
    continue_program = True

    while continue_program:

        # -------------------------
        # Activity 1: Input validation loop
        # -------------------------
        valid_input = False

        while not valid_input:

            user_choice = input(
                "Press Enter to calculate BMI or type 'q' to quit: "
            )

            if user_choice.lower() == 'q':
                continue_program = False
                break

            try:
                weight_lbs = float(input("Enter your weight in pounds: "))
                height_feet = int(input("Enter your height (feet): "))
                height_inches = int(input("Enter remaining height (inches): "))

                if weight_lbs <= 0:
                    raise ValueError("Weight must be greater than zero.")

                if height_feet < 0 or height_inches < 0:
                    raise ValueError("Height values cannot be negative.")

                # Convert total height to inches
                total_height_inches = (height_feet * 12) + height_inches

                if total_height_inches <= 0:
                    raise ValueError("Total height must be greater than zero.")

                valid_input = True  # input is valid

            except ValueError as ve:
                print("\nINPUT ERROR:", ve)
                print("Please try again.\n")

        if not continue_program:
            break

        # Calculate BMI
        bmi = calculate_bmi(weight_lbs, total_height_inches)
        bmi_category = determine_bmi_category(bmi)
        
        # Output formatted to one decimal place
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Category: {bmi_category}\n")

        # Ask whether to continue
        answer = input("Would you like to calculate another BMI? (y/n): ")
        if answer.lower() != 'y':
            continue_program = False

    # -------------------------
    # Activity 4: BMI Table
    # -------------------------
    print("\nBMI Table")
    print("Heights: 58–76 inches (step 2)")
    print("Weights: 100–250 pounds (step 10)\n")

    print(f"{'Weight':<8}", end="")
    for height in range(58, 77, 2):
        print(f"{height:>8}", end="")
    print()

    for weight in range(100, 251, 10):
        print(f"{weight:<8}", end="")
        for height in range(58, 77, 2):
            bmi_value = calculate_bmi(weight, height)
            print(f"{bmi_value:>8.1f}", end="")
        print()

    print("\nProgram terminated.")

main()
