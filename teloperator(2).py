import re
def gsm_operator_bul(num):
    pattern ="\d{11}"
    eslesme = re.search(pattern,num)
    
    if eslesme:
        gsm = str(eslesme.group())
       
        
        if gsm.startswith("054"):
            print("vodafone")
        
        elif gsm.startswith("050"):
            print("Turk Telekom")

        elif gsm.startswith("053"):
            print("Turkcell")

        else:
            print("sebeke bulunamadı")
    else:
        print("eslesme bulunamadı")


a=input("Bir telefon numarasi giriniz\n")
gsm_operator_bul(a)

