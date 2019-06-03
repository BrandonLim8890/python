import re, pyperclip

url_regex = re.compile(r'(http)(s)?(://)(.+)/')
text = str(pyperclip.paste())
matches = []

for group in url_regex.findall(text):
    website = ''.join(group)
    matches.append(website)

pyperclip.copy('\n'.join(matches))

print('\n'.join(matches))