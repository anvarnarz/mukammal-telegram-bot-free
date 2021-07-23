import requests

from pprint import pprint as print

app_id = "62b446b5"
app_key = "c2fe6960887f53b88999a767283d7e34"
language = "en-gb"

word_id = "orange"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()


r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)
res = r.json()
# print(res)

print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])

# word_id = "apples"
# urlLemma = "https://od-api.oxforddictionaries.com:443/api/v2/lemmas/" + language + "/" + word_id.lower()
# rLemma = requests.get(urlLemma, headers={"app_id": app_id, "app_key": app_key})
# result = rLemma.json()
# print(result)
# #pron = json_extract(result, 'audioFile')
# #print(pron)