# Simple CSV → Excel (Excel can open CSV)

data = [
    ["Name", "Age", "City"],
    ["Ali", "20", "Karachi"],
    ["Sara", "22", "Lahore"],
    ["Ahmed", "25", "Islamabad"]
]

file_name = "output.csv"

with open(file_name, "w") as file:
    for row in data:
        file.write(",".join(row) + "\n")

print("✅ File created:", file_name)
print("👉 Open this file in Excel")