import os
from pathlib import Path

print(os.listdir(os.path.join(os.getcwd(), 'files')))

p = Path(Path.cwd()) / 'files'
for item in p.iterdir():
    print(f'{item = }')
