import os
from pathlib import Path

os.remove(os.path.join(os.getcwd(), 'files', '2'))

Path(Path.cwd() / 'files' / '1').unlink()
