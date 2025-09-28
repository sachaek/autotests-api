import json

json_data = """
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "Qa Automation",
    "API Testing"
  ],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}"""
parsed_data = json.loads(json_data)
print(parsed_data)

data = {
    'name': 'Иван',
    'age': 30,
    'is_student': False
}
json_from_dict = json.dumps(data, indent=4)
print(json_from_dict)

with open("json_example.json", "r", encoding='utf-8') as file:
    read_data = json.load(file)
    print(data)

with open("json_example2.json", "w", encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
