#! python
# ================================================== #
# An insecure password locker program                #
# Date: 20171217                                     #
# Author: dieng                                      #
# ================================================== #

pw = {'email': 'uvc87a8sdfjkvcu89asdf',
      'blog': 'ajksivkkjsafijkvcasdfs',
      'luggage': 71807877891074839247}

import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in pw:
    print("Password is " + pw[account])
else:
    print('There is no account named ' + account)