import pytest
import bmi_calculator 

# --- Valid BMI calculations ---
def test_normal_bmi():
    bmi = bmi_calculator.calculate_bmi(150, 67)
    category = bmi_calculator.determine_bmi_category(bmi)
    assert round(bmi, 1) == 23.5
    assert category == "Normal weight"

def test_underweight_bmi():
    bmi = bmi_calculator.calculate_bmi(100, 67)
    category = bmi_calculator.determine_bmi_category(bmi)
    assert round(bmi, 1) == 15.7
    assert category == "Severely Underweight"

def test_overweight_bmi():
    bmi = bmi_calculator.calculate_bmi(200, 67)
    category = bmi_calculator.determine_bmi_category(bmi)
    assert round(bmi, 1) == 31.3
    assert category == "Overweight"

# --- Invalid input tests ---
def test_zero_height():
    with pytest.raises(ZeroDivisionError):
        bmi_calculator.calculate_bmi(150, 0)

def test_invalid_type_height():
    # Passing string instead of number should raise TypeError
    with pytest.raises(TypeError):
        bmi_calculator.calculate_bmi(150, "sixty")
