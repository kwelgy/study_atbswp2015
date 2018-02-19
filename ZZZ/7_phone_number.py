# ================================================== #
# Get clipboard text and extract phone numbers and   #
# emails                                             #
# Date: 20171228                                     #
# Author: dieng                                      #
# ================================================== #
import re
import pyperclip

def get_phone(string):
    phoneRegex = re.compile(r'''(
                           (\d{3}|\(\d{3}\))?               # area code
                           (\s|-|\.)?                       # separator
                           (\d{3})                          # first 3 digits
                           (\s|-|\.)?                       # separator
                           (\d{4})                          # last 4 digits
                           (\s*(ext|x|ext.)\s*\d{2,5})?     # extension
                           )''', re.VERBOSE)
    result = phoneRegex.findall(string)
    return result


def get_email(string):
    emailRegex = re.compile(r'(\w+@\w+\.\w+)')
    result = emailRegex.findall(string)
    return result


txt = str(pyperclip.paste())

phones = [t[0] for t in get_phone(txt)]
emails = get_email(txt)
pyperclip.copy('\n'.join(phones+emails))