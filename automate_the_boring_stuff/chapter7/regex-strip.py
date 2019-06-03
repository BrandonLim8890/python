import re

def regexStrip(text):
    strip_start = re.compile(r'(^\s*)') # Start whitespace removed
    strip_end = re.compile(r'(\s*$)') # End whitespace removed
    text_start_stripped = strip_start.sub('', text)
    text_stripped = strip_end.sub('', text_start_stripped)

    return text_stripped

print('Enter a word:')
striped_word = str(input())
print(regexStrip(striped_word))