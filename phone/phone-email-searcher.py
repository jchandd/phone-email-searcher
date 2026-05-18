#Phone and Email Searcher
# This program will search a peice of text you get from clipboard and parse it for phone numbers and email adresses.
# It will put only phone numbers and email addresses it found into the clipboard
# While doing this project make sure to use regular expressions to find the phone numbers and email addresses
# You can use the re module in python to work with regular expressions

import pyperclip
import re

# Phone Number Regex
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

# Email regex
emailRegex = re.compile(r'''
(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)
''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []

# Find phone numbers
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # groups[1] is the area code, groups[3] is the first 3 digits, and groups[5] is the last 4 digits. We join them with a hyphen to create a standard phone number format.

    if groups[8] != '':
        phoneNum += ' x' + groups[8] # If there is an extension, we add it to the phone number with an 'x' before it.

    matches.append(phoneNum) 

# Find email addresses
for groups in emailRegex.findall(text): # emailRegex.findall() returns a list of tuples, where each tuple contains the matched groups. In this case, we are interested in the first group, which is the entire email address. Therefore, we append groups[0] to the matches list.
    matches.append(groups[0])

