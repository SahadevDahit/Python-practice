import json

# Parse the JSON string
result = '{"name":"sahadev","rollno":"32","address":"kathmandu"}'
res = json.loads(result)

# Print the value associated with the key "name"
print(res["rollno"])

# Define a Python dictionary
Employee = {
    "name": "sanju",
    "department": "IT",
    "salary": "50000"
}

# Convert the Python dictionary to a JSON string and print it
print(json.dumps(Employee))
