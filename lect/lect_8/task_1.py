import json

with open('task_1.json', 'r', encoding='utf-8') as file:
    json_file = json.load(file)

print(type(json_file))
