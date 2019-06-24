#! python3
# delete-unneeded-files.py - Deletes large files or folders that have
# a file size of more than 100MB

import os

root = os.path.abspath('.')


# Walk the current directory and isolate large files
def findLargeFiles(root):
    for file in os.listdir(root):
        file_path = os.path.join(root, file)
        if os.path.isdir(file_path):
            size = getDirSize(file_path)
        else:
            size = os.path.getsize(file_path)
            
        if size > 100:
            print(f'{file_path}: {size}')



# Find the total size of a folder and its contents

def getDirSize(start_path):
    size = 0
    
    for folder_name, sub_folders, file_names in os.walk(start_path):
        for file in file_names:
            file_path = os.path.join(folder_name, file)
            size += os.path.getsize(file_path)        
    
    return size

findLargeFiles(root)