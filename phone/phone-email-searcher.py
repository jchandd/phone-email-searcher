#Phone and Email Searcher
# This program will search a peice of text you get from clipboard and parse it for phone numbers and email adresses.
# It will put only phone numbers and email addresses it found into the clipboard
# While doing this project make sure to use regular expressions to find the phone numbers and email addresses
# You can use the re module in python to work with regular expressions

import re
import pyperclip


def find_vin_numbers():
    # Get text from clipboard
    text = pyperclip.paste()

    # Define regex pattern for VIN numbers
    vin_regex = re.compile(r'\b[A-HJ-NPR-Z\d]{17}\b')

    # Find all matches of VIN numbers in text
    vin_numbers = vin_regex.findall(text)

    # Return list of VIN numbers
    return vin_numbers


print(find_vin_numbers())





















