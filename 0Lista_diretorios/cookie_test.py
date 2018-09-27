import requests

site = 'http://energypriston.com/login'

for a in range(111):
    session = requests.session()
    r  = session.get(site)
    print(session.cookies.get_dict())
    session.close()
