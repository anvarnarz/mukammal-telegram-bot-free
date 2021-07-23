import requests
from jsonExtract import jsonExtract

from pprint import pprint as print

city='tashkent'

url = f"https://api.pray.zone/v2/times/today.json?city={city}&school=2"


r = requests.get(url)
print(r.status_code)
res = r.json()
# print(res)
# print(res['results'])
# print(res['results']['datetime'][0]['times'])
print(jsonExtract(res,'school'))