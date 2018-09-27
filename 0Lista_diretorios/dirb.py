import sys
import requests
import re
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/532.36 (KHTML, like Gecko) Chrome/44.0.2228.0 Safari/537.36"}
v = 0
def rato():
    print("Testando : http://"+sys.argv[1]+"\n")
    f = open("wordlists\\rato.txt")
    site = sys.argv[1]
    for i in f:
        session = requests.session()
        try:
            i = i.strip()
            a = "http://"+i+site
            r = requests.get(url=a)
            print(a)
            print(r.status_code)
        except:
            continue
    sys.exit()
#Apenas checa se a pessoa digitou certo
try:
    if "-v" in sys.argv[3]:
        v = 1
        print("                 VERBOSE ON")
except:
    print("")
try:
    site = sys.argv[1]
    try:
        ratao = 0
        print(sys.argv[2])
        diretorio = "wordlists\\"+sys.argv[2]
        if "-v" in sys.argv[2]:
            v = 1
            print("                 VERBOSE ON")
            diretorio = "wordlists\\medium.txt"
        if "-rato" in str(sys.argv[2]):
            ratao = 1
            sys.exit()
    except:
        diretorio = "wordlists\\medium.txt"

except:
    print("\n                        [+]MODO DE USO\n\
    \n\
    dirb.py site [wordlist]           - Descobre diretorios de um site\n\
    dirb.py site -rato                - Descobre dominios de um site\n\
    -v                                - Verbose\n\
    []OPCIONAL")
    sys.exit()

if ratao  == 1:
    rato()

if "http://" not in site:
    if "https://" not in site:
        site = "http://"+site
print("Site: "+site+"\nWordlist: "+diretorio)
#Usando TOR

tor = input("\n\nDigite algo para utilizar a rede tor(Deixe o tor aberto) >>> ")
tor_on = len(tor)
if tor_on > 0:
    tor_on = "ON"
else:
    tor_on = "OFF"

session = requests.Session()
if len(tor)>0:


    session = requests.Session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9150'
    session.proxies['https'] = 'socks5h://localhost:9150'
tor = int(len(tor))
if tor>0:
    r = session.get("http://httpbin.org/ip")
else:
    r = requests.get("http://httpbin.org/ip")
print("Seu IP: "+str(re.findall("[.\d]+",r.text)))

#Inicio das requests
f = open(diretorio)
for line in f:
    if v == 1:
        print(site+"/"+line,end="")
    r = session.get(url = site+"/"+line, headers = headers, timeout = 10)
    if r.status_code != 404 and r.status_code != 400:
        print(site+"/"+line, end="")
        print(r.status_code)
