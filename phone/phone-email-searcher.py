#Phone and Email Searcher
# This program will search a peice of text you get from clipboard and parse it for phone numbers and email adresses.
# It will put only phone numbers and email addresses it found into the clipboard
# While doing this project make sure to use regular expressions to find the phone numbers and email addresses
# You can use the re module in python to work with regular expressions

import re
import pyperclip
# Get the text from the clipboard
text = pyperclip.paste()
# Create a regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                       # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)               
# Create a regex for email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)  
# Find all the matches in the text and put them in a list
matches = []for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# Copy the results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')



















