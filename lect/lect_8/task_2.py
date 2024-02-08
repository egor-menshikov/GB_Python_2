import json

json_text = """
[{"jdsaf" : 1},
{"dgreger" :"safqf"}
]
"""

json_list = json.loads(json_text)

print(json_list)