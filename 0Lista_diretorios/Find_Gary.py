import requests





url = "https://www.hackthissite.org/missions/realistic/8/login2.php"
#headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

cookies={"accountUsername":"luied", "accountPassword":"4321", "PHPSESSID":"kb7o64effj8vcve10o8m3ft723"}

session = requests.session()
session.headers.update({'referer': "https://www.hackthissite.org/missions/realistic/8/login1.php"})
session.get(url)

r = session.post(url=url,  data={"username":"luied","password":"4321"}, cookies=cookies, allow_redirects=1)

print(r.text)
print(session.cookies.get_dict)
