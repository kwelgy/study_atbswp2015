#!/usr/bin/env python3
import requests, logging
from pprint import pprint

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def excerciseOne():
    res = requests.get('http://gutenberg.org/cache/epub/1112/pg1112.txt')
    assert type(res) == requests.models.Response, "Type not Response!"
    assert res.status_code == requests.codes.ok, "Status code not OK!"
    print(res.text[:10])

def excerciseTwo():
    res = requests.get('http://gutenberg.org/page-that-doesn-not-exist')
    logging.debug(res.raise_for_status())

excerciseTwo()