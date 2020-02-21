import requests
import json
from urllib import request


url = r'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2/10-%D0%B4%D0%BD%D1%96%D0%B2'

url1 = request.urlopen(url)
print(type(url1))
content = url1.read().decode(url1.info().get_param('charset' or 'utf-8'))
print(type(content))

with open('123.json', 'w') as f:
    data = json.dump(content, f, indent=4)