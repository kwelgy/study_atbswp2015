#! python3
# mapIt.py - Lauches a map in a browser using address from command line or clipboard

import webbrowser, sys, logging, pyperclip

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def getAddr():
    if len(sys.argv) > 1:
        # Get address from command line
        addr = ' '.join(sys.argv[1:])
        logging.debug('Getting address from CLI: ' + addr)
    else:
        # Get address from clipboard
        addr = pyperclip.paste()
        logging.debug('Getting address from clipboard: ' + addr)
    return addr


def convertAddr(addr):
    assert len(addr) > 1, 'Address must be at least 2 characters'
    addr = '+'.join(addr.split(' '))
    logging.debug('Convert address to url format: ' + addr)
    return addr


if __name__ == '__main__':
    logging.debug('PROGRAM START')
    address = getAddr()
    convertAddr(address)
    webbrowser.open('http://google.com/maps/place/{0}'.format(address))