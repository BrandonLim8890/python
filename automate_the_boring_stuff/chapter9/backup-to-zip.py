#! python3
# backup-to-zip.py - Copies an entire folder and its contents into
# a ZIP file whos filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of 'folder' into a ZIP file.
    
    folder = os.path.abspath(folder)    # ensures folder is absolute path
    
    
    # Figure out the filename this code should be based on
    # what files already exist.
    
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number += 1
        
    # Create the ZIP file.
    print(f'Creating {zip_file_name}')
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')
    
    # Walk the entire folder tree and compress the files in each folder.
    for folder_name, sub_folders, file_names in os.walk(folder):
        print(f'Adding files in {folder_name}')
        # Add the current folder to the ZIP file.
        backup_zip.write(folder_name)
        # Add all the files in this folder to the ZIP file.
        for file in file_names:
            new_base = os.path.basename(folder) + '_'
            if file.startswith(new_base) and file.endswith('.zip'):
                continue    # don't backup ZIP files
            backup_zip.write(os.path.join(folder_name, file))
    backup_zip.close()
    print('Done.')
    

backupToZip('C:\\delicious')