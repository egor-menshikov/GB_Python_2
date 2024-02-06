import os
from pathlib import Path

# os.replace('files/task_5', os.path.join(os.getcwd(), 'files', 'new_os_dir', 'task_5'))

old_file = Path(Path.cwd() / 'files' / 'task_5')
old_file.replace(Path.cwd() / 'files' / 'new_Path_dir' / 'task_5')