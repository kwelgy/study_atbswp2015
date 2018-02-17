#! python3
# ================================================== #
# Wiki Markup                                        #
# Date: 20171217                                     #
# Author: dieng                                      #
# ================================================== #

import pyperclip

text = pyperclip.paste()

text = text.split('\n')
text = ['* ' + t for t in text]
text = '\n'.join(text)

pyperclip.copy(text)