#! python3

import os, re

if os.path.isfile('madlibs.txt') is False:
    new_madlibs_file = open('madlibs.txt', 'w')
    new_madlibs_file.write('The ADJECTIVE panda walked to the NOUN and then VERB.' + 
                           ' A nearby NOUN was unaffected by these events.')

madlibs_file = open('madlibs.txt')
output_file = open('output.txt', 'w')
madlibs_content = madlibs_file.read()
regex = re.compile(r'(NOUN|ADJECTIVE|ADVERB|VERB)')

matches = regex.findall(madlibs_content)

for match in matches:
    switch = input(f'Enter a {match}: ')
    madlibs_content = madlibs_content.replace(match, switch, 1)

output_file.write(madlibs_content)

print(madlibs_content)
