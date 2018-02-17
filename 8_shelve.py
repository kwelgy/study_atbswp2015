import shelve

## writing to shelve ##
#######################

# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

## reading from shelve ##
#########################

# shelfFile = shelve.open('mydata')
# print(shelfFile['cats'])
# shelfFile.close()

## accessing keys ##
####################

# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()

## pprint.pformat() ##
######################

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('8_myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()