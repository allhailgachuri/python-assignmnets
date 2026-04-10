# -----------------------------
# QUESTION 1: FUNDAMENTALS
# -----------------------------
print("QUESTION 1")

# (a) Definitions
print("\n(a) Definitions:")
print("Variable: A container used to store data. Example: x = 10")
print("Data Type: Defines the type of data. Example: int, str")
print("Function: A reusable block of code. Example: def add():")
print("Module: A file containing Python code. Example: import random")
print("Exception: An error that occurs during execution. Example: division by zero")

# (b) Differences
print("\n(b) Differences:")
print("List vs Tuple: List is mutable, Tuple is immutable")
print("Dictionary vs Set: Dictionary stores key-value pairs, Set stores unique values")

# (c) Output
print("\n(c) Output:")
x = "5"
y = int(x)
z = y * 2
print("Output:", z)
print("Explanation: '5' is converted to integer 5, then multiplied by 2 = 10")

# (d) Error correction
print("\n(d) Error Correction:")
print("Correct Code:")
print("""
number = int(input("Enter number: "))
print(number + 10)
""")


# -----------------------------
# QUESTION 2: CONTROL STRUCTURES & FUNCTIONS
# -----------------------------
print("\nQUESTION 2")

# (a) Grade system
marks = int(input("\nEnter student's marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# (b) Function
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

sample_data = [10, 20, 30, 40]
total, avg = calculate_stats(sample_data)

print("\nFunction Demo:")
print("Numbers:", sample_data)
print("Total:", total)
print("Average:", avg)


# -----------------------------
# QUESTION 3: DATA STRUCTURES
# -----------------------------
print("\nQUESTION 3")

# (a) Loop through scores
scores = [45, 78, 62, 49, 85, 90]

pass_count = 0
fail_count = 0

for score in scores:
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Passed:", pass_count)
print("Failed:", fail_count)

# (b) Dictionary
students = {
    "Alice": 75,
    "Bob": 45,
    "Charlie": 65,
    "David": 55
}

print("\nAll Students:")
for name, mark in students.items():
    print(name, ":", mark)

print("\nStudents scoring above 60:")
for name, mark in students.items():
    if mark > 60:
        print(name, ":", mark)


# -----------------------------
# QUESTION 4: MODULES, FILES & EXCEPTIONS
# -----------------------------
print("\nQUESTION 4")

import random

# (a) Generate numbers
numbers = [random.randint(1, 100) for _ in range(10)]
print("Generated Numbers:", numbers)

# (b) Save to file
with open("data.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

print("Data saved to file.")

# (c) Read file
try:
    with open("data.txt", "r") as file:
        data = file.readlines()
    print("File contents:", data)
except FileNotFoundError:
    print("File not found.")

# (d) Exception handling
try:
    numbers_read = [int(line.strip()) for line in data]
    print("Processed Numbers:", numbers_read)
except ValueError:
    print("Invalid data found in file.")


# -----------------------------
# QUESTION 5: OOP & JSON
# -----------------------------
print("\nQUESTION 5")

# (a) Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_result(self):
        if self.marks >= 50:
            result = "Pass"
        else:
            result = "Fail"
        print(self.name, "-", result)

# Create objects
student1 = Student("John", 65)
student2 = Student("Mary", 40)

student1.display_result()
student2.display_result()

# (b) JSON handling
import json

student_data = {
    "students": [
        {"name": "John", "marks": 65},
        {"name": "Mary", "marks": 40}
    ]
}

# Save JSON
with open("students.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("Student data saved to JSON.")

# Read JSON
with open("students.json", "r") as file:
    loaded_data = json.load(file)

print("\nJSON Data:")
for student in loaded_data["students"]:
    print(student["name"], "-", student["marks"])