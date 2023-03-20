from os import link
import requests
import json

bilgi_link="https://www.akyazihaber.com/ilanlar/yanlis-duymadiniz-sadece-10-tl-57848-detay"

dönüt=requests.get(bilgi_link)

print(dönüt.status_code)
print(dönüt.url)
print(dönüt.text)
dönüt.json()





