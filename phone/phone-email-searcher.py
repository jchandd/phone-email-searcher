#Phone and Email Searcher
# This program will search a peice of text you get from clipboard and parse it for phone numbers and email adresses.
# It will put only phone numbers and email addresses it found into the clipboard
# While doing this project make sure to use regular expressions to find the phone numbers and email addresses
# You can use the re module in python to work with regular expressions
# make somewhere for the user to input the text they want to search through, or you can use the clipboard to get the text


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


# Email Address Regex
emailRegex = re.compile(r'''
(
    [a-zA-Z0-9._%+-]+ # username
    @                 # @ symbol
    [a-zA-Z0-9.-]+    # domain name
    \.[a-zA-Z]{2,}    # dot-something
)
''', re.VERBOSE)



# Get text from user input
text = input('Paste text to search for phone numbers and emails: ')

matches = []
found_phones = set()
found_emails = set()

# Find phone numbers
for groups in phoneRegex.findall(text): # groups is a tuple of all the matched groups in the regex
    area = groups[1] if groups[1] else ''
    first3 = groups[3]
    last4 = groups[5]
    phoneNum = '-'.join(filter(None, [area, first3, last4])) # filter out empty strings and join with dashes
    if groups[8]:
        phoneNum += ' x' + groups[8] # Add extension if it exists
    if phoneNum and phoneNum not in found_phones:
        matches.append(phoneNum) # Add the phone number to the matches list if it's not empty and not already found
        found_phones.add(phoneNum)

# Find email addresses
for groups in emailRegex.findall(text):
    email = groups[0]
    if email not in found_emails:
        matches.append(email)
        found_emails.add(email)

# Copy results to clipboard
if matches:
    pyperclip.copy('\n'.join(matches)) # Join the matches with newlines and copy to clipboard
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

