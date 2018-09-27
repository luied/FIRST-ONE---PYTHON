import requests
import re
import sys
import shutil
import os
import time
from pprint import pprint

try:
    criar = ["Company_emails.txt","Company_emails_cache.txt","emails.txt","Filtrar.txt"]
    for a in criar:
        open(a,"x")
        print("Arquivo "+a+" criado")
        a.close()
except:
    print("")

file = open("Filtrar.txt","r")
a = ""
b = []
g = []
numero=1
for linha in file:

    emails = (re.findall(r'[^ ]+@\w*.com[/\. ]?b?r?' , linha))
    if len(str(emails)) > 5:
        ala = "\n".join(emails)
        ala = re.sub(r"[/]", r"\n", ala)
        ala = re.sub(r"\.$", r"\n", ala)
        ala = re.sub(r"[/]&", r"\n", ala)
        ala = re.sub(r"\.$", r"", ala)
        ala = re.sub(r" ", r"\n", ala)
        ala = re.sub(r"\n\n", r"\n", ala)
        ala = re.sub(r" ", r"\n", ala)
        ala = re.sub(r"\n\n", r"\n", ala)
        #print("".join(emails),end="\n")
        if ala not in b:
            b.append(ala)
        else:
            continue
        f = open("Company_emails_cache.txt","r")
        if not re.findall(str(ala),f.read()):
            f.seek(0)
            try:
                print(ala)
                g.append(ala)
            except:
                pass
        else:
            f.seek(0)


        f.close()

deseja = input("\n\n[+]DESEJA SALVAR OS EMAILS NOS ARQUIVOS: \n\n>Company_emails_cache.txt\n>Company_emails.txt\n\n[Y/n]")
if "n" in deseja:
    sys.exit()

else:
    print("Salvo")
    f = open("Company_emails_cache.txt","a")
    for linhaa in g:
        f.write(linhaa+"\r\n")
    f.close()
#---------------------------------------------------
    f = open("Company_emails.txt","a")
    for linhaa in g:
        f.write(linhaa+"\r\n")
    f.close()
#--------------------------------------------------
    f = open("emails.txt","w")
    for linhaa in g:
        f.write(linhaa+"\r\n")
    f.close()


"""
copie a pagina e coloque em Filtrar.txt
Ele printa na tela os emails que nao estao no arquivo Company_emails_cache.txt
"""


        #numero+=1
        #print(numero)
