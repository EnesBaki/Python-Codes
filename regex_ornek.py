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
##  \     ESC         (SELAM)    \(\w{3}\)    karakterin özelliğini bırakıp sadece text olarak okunmasını sağlar
import re

def mesaj_hissi(cumle):
    hisler=[]

    pozitif_pattern="yaşası+n|merhaba|selam|ask|sev|tabi+|tamam|ok"
    
    negatif_pattern="olmaz|hayır|yapamam|edemem|gidemem|[M|m]aalesef|üzgünüm"

    heyecanlı_pattern="!|yaşası+n|\?|:\)+"

    emin_pattern= "[k|K]esin|[T|t]abi+"

    karasız_pattern= "[b,B]elki|[s,S]anırım"

    if re.search(pozitif_pattern,cumle):
        hisler.append("pozitif")
        
    if re.search(negatif_pattern,cumle):
        hisler.append("negatif")
    
    if re.search(heyecanlı_pattern,cumle):
        hisler.append("heyecanlı")

    if re.search(emin_pattern,cumle):
        hisler.append("emin")

    if re.search(karasız_pattern,cumle):
        hisler.append("kararsız")

    print(hisler)

cumle1="Merhaba, sanırım kar yağacak?"
cumle2="Tabii, memnun olurum:))"
cumle3="Maalesef, en kısa sürede bekliyorum"


mesaj_hissi(cumle1)
mesaj_hissi(cumle2)
mesaj_hissi(cumle3)