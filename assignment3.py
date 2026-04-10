import random
import json

# -----------------------------
# QUESTION 1: Data Generation
# -----------------------------
print("QUESTION 1: Data Generation")

numbers = [random.randint(10, 100) for _ in range(15)]
print("Generated Numbers:", numbers)

total = sum(numbers)
average = total / len(numbers)

print("Total:", total)
print("Average:", average)


# -----------------------------
# QUESTION 2: File Writing
# -----------------------------
print("\nQUESTION 2: Writing to File")

try:
    with open("data.txt", "w") as file:
        for num in numbers:
            file.write(str(num) + "\n")
    print("Data successfully saved to data.txt")
except Exception as e:
    print("Error writing to file:", e)


# -----------------------------
# QUESTION 3: File Reading & Analysis
# -----------------------------
print("\nQUESTION 3: Reading and Analysis")

try:
    with open("data.txt", "r") as file:
        data = file.readlines()

    numbers_from_file = [int(line.strip()) for line in data]

    print("Numbers from file:", numbers_from_file)
    print("Maximum:", max(numbers_from_file))
    print("Minimum:", min(numbers_from_file))
    print("Average:", sum(numbers_from_file) / len(numbers_from_file))

except FileNotFoundError:
    print("Error: data.txt file not found.")
except ValueError:
    print("Error: File contains non-numeric data.")


# -----------------------------
# QUESTION 4: Exception Handling
# -----------------------------
print("\nQUESTION 4: Exception Handling")

try:
    with open("data.txt", "r") as file:
        data = file.readlines()

    numbers_safe = []

    for line in data:
        try:
            num = int(line.strip())
            numbers_safe.append(num)
        except ValueError:
            print("Invalid data skipped:", line.strip())

    if numbers_safe:
        print("Max:", max(numbers_safe))
        print("Min:", min(numbers_safe))
        print("Average:", sum(numbers_safe) / len(numbers_safe))

except FileNotFoundError:
    print("Error: data.txt file not found.")


# -----------------------------
# QUESTION 5: JSON Handling
# -----------------------------
print("\nQUESTION 5: JSON Storage")

data_dict = {
    "data": numbers,
    "total": total,
    "average": average
}

try:
    with open("data.json", "w") as json_file:
        json.dump(data_dict, json_file, indent=4)

    print("Data saved to data.json")

    with open("data.json", "r") as json_file:
        loaded_data = json.load(json_file)

    print("JSON Data:")
    print("Numbers:", loaded_data["data"])
    print("Total:", loaded_data["total"])
    print("Average:", loaded_data["average"])

except Exception as e:
    print("JSON error:", e)

 