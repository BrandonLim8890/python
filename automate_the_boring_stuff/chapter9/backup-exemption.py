#! python3
# backup-exemption.py - Archives a folder but exemps the given extension

import os, zipfile

abs_path = os.path.abspath('.')

def backupExemption(extension):
    zip_file_name = os.path.basename(abs_path) + '.zip'
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')
    for folder_name, sub_folders, file_names in os.walk(abs_path):
        print(f'Adding {folder_name} to zip')
        backup_zip.write(folder_name)
        for file in file_names:
            if file.endswith(extension):
                continue
            print(f'Adding {file} to zip')
            backup_zip.write(file)
    
    backup_zip.close()
    print('Finished')

print('This program archives a folder but exempts a given file extension.\nChoose a file extension: ')
ext = input()

backupExemption(ext)