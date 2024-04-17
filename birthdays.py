import json
data = [{"name": "John Doe", "birth_month": "10", "birth_date": "15"}, {"name": "Jane Smith", "birth_month": "12", "birth_date": "5"}]

# Specify the file path
file_path = "birthdays.json"

# Write data to the JSON file
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)