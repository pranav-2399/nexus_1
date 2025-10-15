import json

data = [
    {
        "name": "ABC",
        "rollNo": 1234,
        "marks": 90
    }
]
with open("student_details.json", "w") as f:
    json.dump(data, f, indent = 4)

newData = {
    "name": "DEF",
    "rollNo": 3210,
    "marks": 95
}

data.append(newData)

""" with open("student_details.json", "w") as f:
    json.dump(data, f, indent = 4) """

for i in data:
    print(i)