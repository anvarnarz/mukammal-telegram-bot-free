# https://github.com/fawazahmed0/quran-api
import requests
from pprint import pprint as print

sura=1
oyat=4
tafsir='uzb-muhammadsodikmu'

url_sura=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}.json"
url_oyat=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"

r = requests.get(url_oyat)
print(r.status_code)
res = r.json()
print(res)