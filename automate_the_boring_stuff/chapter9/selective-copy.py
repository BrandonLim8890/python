#! python3
# selective-copy.py - A program that walks through a folder tree and searches
# for files with a certain file extension. Copies these files to a new folder

import os, shutil

cur_folder = os.path.abspath('.')

def selectiveCopy(extension, dest_folder_name):
    dest_folder = cur_folder + '\\' + dest_folder_name
    os.mkdir(dest_folder)
    print(f'Created {dest_folder_name} at {dest_folder}')
    
    for folder_name, sub_folders, file_names in os.walk('.'):
        for file in file_names:
            if file.endswith(extension):
                print(f'Copying over {file} to {dest_folder}')
                shutil.copy(folder_name + '\\' + file, dest_folder)
    print('done')
    
selectiveCopy('.py', 'python_files')