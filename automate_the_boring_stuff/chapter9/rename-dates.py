#! python3
# rename-dates.py - Renames filenames with American MM-DD-YYYY date formate
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex taht matches files with the American date format.
date_pattern = re.compile(r"""^(.*?)        # all text before the date
                          ((0|1)?\d)-       # one or two digits for the month
                          ((0|1|2|3)?\d)-   # one or two digits for the day
                          ((19|20)\d[2])    # four digits for the year
                          (.*?)$            # all text after the date
                          """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
for file in os.listdir('.'):
    matched = date_pattern.search(file)
    
#   Skip files without a date.
    if matched is None:
        continue

#   Get the different parts of the filename.
    before_part = matched.group(1)
    month = matched.group(2)
    day = matched.group(4)
    year = matched.group(6)
    after_part = matched.group(8)

#   Form the European-style filename.
    euro_file_name = f'{before_part}{day}-{month}-{year}{after_part}'

#   Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    amer_file_name = os.path.join(abs_working_dir, file)
    euro_file_name = os.path.join(abs_working_dir, euro_file_name)

#   Rename the files.
    print(f'Renaming "{file}" to "{euro_file_name}"')
    # shutil.move(file, euro_file_name)

print('Process finished.')