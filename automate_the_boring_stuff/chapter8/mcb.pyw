#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) is 3:
    if sys.argv[1].lower() is 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    
    elif sys.argv[1].lower() is 'delete':
        
        # Deletes all the keys
        if sys.argv[2].lower() is 'all':
            for key in list(mcb_shelf.keys()):
                del mcb_shelf[key]
                
        # Deletes the specified key
        else:
            del mcb_shelf[sys.argv[2]]
        
elif len(sys.argv) is 2:
    # List keywords and load content.
    if sys.argv[1].lower() is 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()