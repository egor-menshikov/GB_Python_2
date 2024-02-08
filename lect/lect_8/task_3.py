import json

data = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": [
        "кузнечное дело",
        "программирование",
        "путешествия"
    ],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

with open('task_3_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4, separators=(chr(128524), chr(128517)), sort_keys=True)
