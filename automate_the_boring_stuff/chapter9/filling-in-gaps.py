#! python3
# filling-in-gaps.py - Finds all files with a prefix and locates and fixes
# any gaps in the numbering

import os, re, shutil

root = os.path.abspath('.')

# Find all files and locate gaps
def findGaps(prefix):
    file_regex = re.compile(prefix + r'(\d+)')
    file_list = []
    for file in os.listdir(root):
        if file_regex.match(file):
            file_list.append(file)
            print(f'{file} added to list')
    file_list.sort()
    return file_list


# Fixes and closes the gaps
def fillGaps(prefix):
    file_list = findGaps(prefix)
    file_regex = re.compile(prefix + r'(\d+)(\w+)')
    
    start_index = int(file_regex.search(file_list[0].group(1)))
    count = start_index
    
    for file in file_list:
        matched = file_regex.search(file)
        file_num = int(matched.group(1))
        
        if file_num != count:
            new_file_name = prefix + str(count) + matched.group(2)
            shutil.move(os.path.abspath(file), os.path.abspath(new_file_name))
        count += 1