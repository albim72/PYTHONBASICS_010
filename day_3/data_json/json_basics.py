import json

# JSON data (in real projects, this could come from a file or an API)
data_json = """
{
  "employees": [
    {"name": "Alice", "department": "Sales", "salary": 4200},
    {"name": "Bob", "department": "IT", "salary": 5100},
    {"name": "Clara", "department": "HR", "salary": 3900},
    {"name": "David", "department": "IT", "salary": 5800}
  ]
}
"""

# Load JSON string into Python dictionary
data = json.loads(data_json)

# Print all employee names
print("Employee names:")
for emp in data["employees"]:
    print("-", emp["name"])

# Calculate average salary
salaries = [emp["salary"] for emp in data["employees"]]
avg_salary = sum(salaries) / len(salaries)

print("\nAverage salary:", avg_salary)
