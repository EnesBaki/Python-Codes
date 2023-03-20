from ast import pattern
import re

cumle="GALATASARAY UEFA KUPASINI KAZANAN TEK TÜRK TAKIMIDIR AYNI ZAMANDA TÜRKİYE'DE 4 YILDIZI OLAN İLK VE TEK KULÜPTÜR"

paternn="TÜRK"  ## EĞER 2 YERDE GEÇİYORSA YALNIZCA İLK KISMIN OLDUĞU YERLERİ GÖSTERİR

print(re.search(paternn,cumle))
print(re.search(paternn,cumle).span())   

for eslesme in re.finditer(paternn,cumle):
    print(eslesme.span(),eslesme.group())


##  \d  rakam   
##  \w  karakter
##  \s  bosluk 
##  \D  RAKAM DEĞİL
##  \W  KARAKTER DEĞİL
##  \S  BOSLUK DEĞİL

## {5}          Adet
## {3,4}        Veya
## {2,}         En az 
##  *           0 Ya da daha fazla
##  +           1 Ya da daha fazla 
##  ?           Ya 1 Ya Hiç

##  |     VE YA
##  ^     BASLAR
##  $     BİTER
##  .     HERHANGİ  
##  \     ESC         (SELAM)    \(\w{3}\) 
text="my phone number 535-1234560"
patern="\d\d\d-\d\d\d\d\d\d\d"
print(re.search(patern,text))