
# extracts email and phone from clipboard text

import re
import pyperclip

# Regex for phone eg. 255-453-5577
phone_reg = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


# Regex for email
emailRegex = re.compile(r'''(
  	[a-zA-Z0-9._%+-]+      # username
  	@                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_reg.findall(text):
	phonenum = '-'.join([groups[1], groups[3], groups[5]])

	if groups[8] != '':
		phonenum += ' x' + groups[8]

	matches.append(phonenum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

# copy to clipboard
if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print('Copied data :')
	print('\n'.join(matches))
else:
	print('Sorry!!! no email and phone number found :(')
