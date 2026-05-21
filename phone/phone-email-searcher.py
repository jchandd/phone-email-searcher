#Phone and Email Searcher
# This program will search a peice of text you get from clipboard and parse it for phone numbers and email adresses.
# It will put only phone numbers and email addresses it found into the clipboard
# While doing this project make sure to use regular expressions to find the phone numbers and email addresses
# You can use the re module in python to work with regular expressions
# make somewhere for the user to input the text they want to search through, or you can use the clipboard to get the text


import pyperclip
import re

# Phone Number Regex Pattern
# Pattern: (area code) + separator + (first 3 digits) + separator + (last 4 digits) + optional (extension)
phoneRegex = re.compile(r'''
(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first 3 digits
    (\s|-|\.)               # separator
    (\d{4})                 # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)
''', re.VERBOSE)


# Email Address Regex
emailRegex = re.compile(r'''
(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,}
)
''', re.VERBOSE)



# Get text from user input
text = input('Paste text to search for phone numbers and emails: ')

matches = []
found_phones = set()
found_emails = set()

# Find phone numbers
for groups in phoneRegex.findall(text):
    area = groups[1] if groups[1] else ''
    first3 = groups[3]
    last4 = groups[5]
    phoneNum = '-'.join(filter(None, [area, first3, last4]))
    if groups[8]:
        phoneNum += ' x' + groups[8]
    if phoneNum and phoneNum not in found_phones:
        matches.append(phoneNum)
        found_phones.add(phoneNum)

# Find email addresses
for groups in emailRegex.findall(text):
    email = groups[0] if isinstance(groups, tuple) else groups
    if email not in found_emails:
        matches.append(email)
        found_emails.add(email)

# Copy results to clipboard
if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

