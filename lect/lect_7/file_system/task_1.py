import os
from pathlib import Path
import shutil

# print(os.getcwd())
# print(Path.cwd())
# os.chdir('../..')
# print(Path.cwd())

# os.mkdir('files/new_os_dir')
# Path('files/new_Path_dir').mkdir()

# os.rmdir('files/new_os_dir')
# Path('files/new_Path_dir').rmdir()

shutil.rmtree('files')