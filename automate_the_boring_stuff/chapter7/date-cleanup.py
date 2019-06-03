import pyperclip, re

text = str(pyperclip.paste())
calendar_regex = re.compile(r'''
    (\d{1,2})
    (/)
    (\d{1,2})
    (/)
    (\d{2,4})
    ''', re.VERBOSE)
matches = []
for group in calendar_regex.findall(text):
    matches.append('-'.join([group[0], group[2], group[4]]))

pyperclip.copy('\n'.join(matches))
print('\n'.join(matches) + 'copied to keyboard')