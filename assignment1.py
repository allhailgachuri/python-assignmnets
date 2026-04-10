# -----------------------------
# QUESTION 1: Personal Data Collection
# -----------------------------
print("QUESTION 1: STUDENT PROFILE")

# Input
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
student = input("Are you a student? (True/False): ")

# Convert student to boolean
student = student == "True"

# Output
print("\n--- STUDENT PROFILE ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Student:", student)

# Display data types
print("\nData Types:")
print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))
print("Student:", type(student))


# -----------------------------
# QUESTION 2: Basic Calculator
# -----------------------------
print("\nQUESTION 2: BASIC CALCULATOR")

# Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

# Output
print("\nResults:")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)


# -----------------------------
# QUESTION 3: Simple Data Analysis
# -----------------------------
print("\nQUESTION 3: DATA ANALYSIS")

# Input
num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))
num3 = float(input("Enter third value: "))

# Calculations
total = num1 + num2 + num3
average = total / 3

# Find largest and smallest
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

# Output
print("\nResults:")
print("Total:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)