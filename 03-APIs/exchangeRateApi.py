# exchangerate-api.com 
import requests
from pprint import pprint as print

API_KEY =  '8d155b29d9f40459f46dd501'

currency='USD'
url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
# print(response.status_code)
# print(response.json())
jsondata = response.json()
kurs = response.json()['conversion_rate']
print(f"Bugungi kurs: 1AQSH dollair = {kurs} so'm")

# res = r.json()
# print(res)
# print(res['conversion_rate'])
