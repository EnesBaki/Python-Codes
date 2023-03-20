import re
from urllib import response
import requests
from PIL import Image
from io import BytesIO


grafik_URL="https://image-charts.com/chart"
##"https://image-charts.com/chart?chan&chd=t%3A60%2C40&chf=ps0-0%2Clg%2C45%2Cffeb3b%2C0.2%2Cf44336%2C1%7Cps0-1%2Clg%2C45%2C8bc34a%2C0.2%2C009688%2C1&chl=Hello%7CWorld&chs=700x190&cht=p3"

payload={
    "chan":None,
    "chd":"t:60,40",
    "chf":"ps0-1,lg,19,7cb54e,0.2,f96376,8|ps0-1,lg,95,8bc34a,0.2,012588,1",
    "chl":"ronaldo|messi",
    "chs":"700x190",
    "cht":"p3"
}

response=requests.post(grafik_URL,payload)

resim=Image.open(BytesIO(response.content))
#print(resim.show())

graph_URL="https://image-charts.com/chart"

load={
    "chco":"3092de",
    "chd":"t:81,65,50,67,59,81",
    "chdl":"First",
    "chdlp":"b",
    "chs":"480x480",
    "cht":"r",
    "chtt":"Futbolcu Özellikleri",
    "chl":"hız|sut|pas|top surme|defans|fizik"}

dönüt=requests.post(graph_URL,load)
görsel=Image.open(BytesIO(dönüt.content))
print(görsel.show())