 # Project 62: Garden Produce Log

from array import array

# --------------------------
# 1. Integers: Quantities of Produce
# --------------------------
produce_quantities = [25, 40, 15, 30, 20]  # example quantities of produce in kilograms

total_quantity = sum(produce_quantities)
average_quantity = total_quantity / len(produce_quantities)
min_quantity = min(produce_quantities)
max_quantity = max(produce_quantities)

print("Integer Calculations:")
print(f"Total Produce Quantity: {total_quantity} kg")
print(f"Average Produce Quantity: {average_quantity:.2f} kg")
print(f"Minimum Produce Quantity: {min_quantity} kg")
print(f"Maximum Produce Quantity: {max_quantity} kg")
print("\n")

# --------------------------
# 2. Strings: Formatted Report
# --------------------------
report = f"Garden Produce Report:\nTotal Quantity = {total_quantity} kg\nAverage Quantity = {average_quantity:.2f} kg"
print(report)

summary = f"Produce Range: {min_quantity} kg - {max_quantity} kg"
print(summary)
print("\n")

# --------------------------
# 3. Booleans: Threshold Check
# --------------------------
threshold = 25
if average_quantity > threshold and max_quantity > threshold:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
print("\n")

# --------------------------
# 4. Lists: Manage Produce Items
# --------------------------
produce_items = ["Tomatoes", "Carrots", "Cabbage", "Lettuce", "Peppers"]
print("Original Produce Items:", produce_items)

# Add a new produce item
produce_items.append("Spinach")
# Remove an item based on a condition (remove "Cabbage")
if "Cabbage" in produce_items:
    produce_items.remove("Cabbage")

# Sort the list
produce_items.sort()
print("Modified Produce Items:", produce_items)
print("\n")

# --------------------------
# 5. Arrays: Store Numeric Quantities
# --------------------------
quantity_array = array('i', produce_quantities[:4])  # take first 4 quantities
sum_array = sum(quantity_array)
print("Array Quantities:", quantity_array.tolist())
print(f"Sum of Array Quantities: {sum_array}")
print(f"Sum of List Quantities (first 4): {sum(produce_quantities[:4])}")
print("\n")

# --------------------------
# 6. Dictionaries: Produce Records
# --------------------------
produce_records = [
    {"id": 1, "name": "Tomatoes", "value": 25},
    {"id": 2, "name": "Carrots", "value": 40},  
    {"id": 3, "name": "Cabbage", "value": 15},
    {"id": 4, "name": "Lettuce", "value": 30},
    {"id": 5, "name": "Peppers", "value": 20}
]

# Update record: Increase Carrots quantity by 10%
for item in produce_records:
    if item["name"] == "Carrots":
        item["value"] = int(item["value"] * 1.1)

# Delete record: Remove Cabbage
produce_records = [item for item in produce_records if item["name"] != "Cabbage"]

# Compute total value from dictionaries
total_value = sum(item["value"] for item in produce_records)

print("Produce Records:")
for item in produce_records:
    print(item)
print(f"Total Quantity from Records: {total_value} kg")