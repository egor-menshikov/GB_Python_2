from pathlib import Path

with open(Path('__init__.py'), 'w', encoding='utf-8') as file:
    file.write("all = ['def save_to_json', 'def find_roots', 'def generate_csv_file']")
