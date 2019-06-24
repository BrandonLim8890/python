#! python3
# extension-archiver.py - Archives files with the inputted file extension

import os, zipfile

folder = os.path.abspath('.')

def extensionArchiver(extension):
    zip_file_name = os.path.basename(folder) + '_archive.zip'
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')
    for folder_name, sub_folders, file_names in os.walk(folder):
        print(f'Adding {folder_name} to zip')
        backup_zip.write(folder_name)
        for file in file_names:
            if file.endswith(extension):
                backup_zip.write(os.path.join(folder_name, file))
                print(f'Adding {file} to archive')
    backup_zip.close()
    
    print('Finished')
    
ext = input('Enter an extension type to archive')
extensionArchiver(ext)