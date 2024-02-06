import os
from pathlib import Path

# os.chdir('files')
# dir_list = os.listdir()
# print(dir_list)

# dir_list = os.listdir(os.path.join(os.getcwd(), 'files'))
# print(dir_list)

# for obj in dir_list:
#     print(f'{os.path.isdir(obj) = } || '
#           f'{os.path.isfile(obj) = } || '
#           f'{os.path.islink(obj) = } || '
#           f'{obj = }')


p = Path(Path.cwd()) / 'files'

for obj in p.iterdir():
    print(f'{obj.is_dir() = } || '
          f'{obj.is_file() = } || '
          f'{obj.is_symlink() = } || '
          f'{obj = }')
