#! python3
# spam-indicator.py - Renames all files in the directory
# to files with 'spam_' in the beginning

import shutil, os, re

regex = re.compile(r'(.txt)$')

for file in os.listdir('.'):
    if regex.search(file) is None:
        continue
    spam_name = f'spam_{file}'
    print(f'Changing {file} to {spam_name}')
    abs_path = os.path.abspath('.')
    file_name = os.path.join(abs_path, spam_name)
    shutil.move(file, file_name)
    