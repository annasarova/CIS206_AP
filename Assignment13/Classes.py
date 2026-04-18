# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:05:50 2026

@author: Anna Sarova
"""
# ============================================================
# EXERCISE 1: EMPLOYEE CLASS
# ============================================================

class Employee:
    # Constructor (acts as default + parameterized)
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    # -------- Mutators --------
    def set_name(self, name):
        self.name = name

    def set_idNumber(self, idNumber):
        self.idNumber = idNumber

    def set_department(self, department):
        self.department = department

    def set_position(self, position):
        self.position = position

    # -------- Accessors --------
    def get_name(self):
        return self.name

    def get_idNumber(self):
        return self.idNumber

    def get_department(self):
        return self.department

    def get_position(self):
        return self.position


# -------- Test Program for Exercise 1 --------
def test_employee():
    print("================================================")
    print("EXERCISE 1 OUTPUT: EMPLOYEE DATA")
    print("================================================\n")

    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    

    employees = [emp1, emp2, emp3]

    for emp in employees:
        print(f"Name: {emp.get_name()}")
        print(f"ID Number: {emp.get_idNumber()}")
        print(f"Department: {emp.get_department()}")
        print(f"Position: {emp.get_position()}")
        print("-" * 40)
    
    employees[2].set_position("Tester")
    
    print("\nChanged Joy's Rogers position from 'Engineer' to 'Tester':\n")
    for emp in employees:
        print(f"Name: {emp.get_name()}")
        print(f"ID Number: {emp.get_idNumber()}")
        print(f"Department: {emp.get_department()}")
        print(f"Position: {emp.get_position()}")
        print("-" * 40)

# ============================================================
# EXERCISE 2: PATIENT & PROCEDURE CLASSES
# ============================================================

class Patient:
    def __init__(self, first, middle, last, address, city, state, zip_code, 
                 phone, emergency_name, emergency_phone):
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    # -------- Mutators --------
    def set_first(self, first):
        self.first = first
        
    def set_middle(self, middle):
        self.middle = middle
        
    def set_last(self, last):
        self.last = last
        
    def set_address(self, address):
        self.address = address
            
    def set_city(self, city):
        self.city = city
        
    def set_state(self, state):
        self.state = state
    
    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_phone(self, phone):
        self.phone = phone

    def set_emergency_name(self, emergency_name):
        self.emergency_name = emergency_name

    def set_emergency_phone(self, emergency_phone):
        self.emergency_phone = emergency_phone  
                  
    # -------- Accessors --------
    def get_first(self):
        return self.first
    
    def get_middle(self):
        return self.middle
    
    def get_last(self):
        return self.last

    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_zip_code(self):
        return self.zip_code

    def get_phone(self):
        return self.phone

    def get_emergency_name(self):
        return self.emergency_name
    
    def get_emergency_phone(self):
        return self.emergency_phone


class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    # -------- Mutators --------
    def set_name(self, name):
        self.name = name
    
    def set_date(self, date):
        self.date = date
        
    def set_practitioner(self, practitioner):
        self.practitioner = practitioner
            
    def set_charge(self, charge):
        self.charge = charge
    
    # -------- Accessors --------
    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_charge(self):
        return self.charge


# -------- Test Program for Exercise 2 --------
def test_patient_procedure():
    from datetime import date

    print("\n================================================")
    print("EXERCISE 2 OUTPUT: PATIENT & PROCEDURES")
    print("================================================\n")

    today = date.today()

    # Create Patient object
    patient = Patient(
        "John", "A.", "Doe",
        "123 Main St", "Chicago", "IL", "60007",
        "555-1234",
        "Jane Doe", "555-5678"
    )

    # Create Procedure objects
    proc1 = Procedure("Physical Exam", today, "Dr. Irvine", 250.00)
    proc2 = Procedure("X-ray", today, "Dr. Jamison", 500.00)
    proc3 = Procedure("Blood test", today, "Dr. Smith", 200.00)

    procedures = [proc1, proc2, proc3]

    # Display Patient Info
    print("PATIENT INFORMATION:\n")
    print(f"Name: {patient.get_first()} {patient.get_middle()} "
          f"{patient.get_last()}")
    print(f"Address: {patient.get_address()}, {patient.get_city()}, "
          f"{patient.get_state()}, {patient.get_zip_code()}")
    print(f"Phone: {patient.get_phone()}")
    print(f"Emergency Contact: {patient.get_emergency_name()} "
          f"({patient.get_emergency_phone()})")

    # Display Procedures
    print("\nPROCEDURE DETAILS:\n")

    total = 0
    for proc in procedures:
        print(f"Procedure: {proc.get_name()}")
        print(f"Date: {proc.get_date()}")
        print(f"Practitioner: {proc.get_practitioner()}")
        print(f"Charge: ${proc.get_charge():.2f}")
        print("-" * 40)
        total += proc.get_charge()

    # Display Total Charges
    print(f"\nTotal Charges: ${total:.2f}")

# ==============================
# MAIN FUNCTION
# ==============================
def main():
    test_employee()
    test_patient_procedure()


# ==============================
# PROGRAM START
# ==============================
# This starts the execution of the program
main()