import os
from pathlib import Path

path1 = os.path.join(os.getcwd(), 'files', 'new_os_dir', 'file.txt')
print(f'{path1 = }')

path2 = Path().cwd() / 'files' / 'new_os_dir' / 'file.txt'
print(f'{path2 = }')

path3 = Path(Path.cwd(), 'dir', 'files')
print(f'{path3 = }\n{path3}')

print(type(path1))
print(type(path2))
