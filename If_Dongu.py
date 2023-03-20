#not ortalamasına göre başarı düzeyleri
#0-50 başarısız
#50-60 yeterli
#60-70 orta
#70-80 iyi
#80-100 çok iyi

not_ort=78 

if not_ort<50:
          print("Başarı Durumu:{}".format("Basarisiz"))

elif 50<not_ort<60:
    print("Basari Durumu:{}".format("Yeterli"))

elif 60<not_ort<70:
    print("Basari Durumu:{}".format("Orta"))

elif 70<not_ort<80:
    print("Basari Durumu:{}ve {}".format("Iyi ","geçer"))

else:
    print("Basari Durumu:{}".format("Cok Iyi"))


#örnek II  Liste içinde öge kontrolü yapma
 


adres={"ülke":"tr",
       "il":"sakarya",
       "ilçe":"akyazı"}

if adres["il"]=="sakarya":
    print("il bilgisi doğru")

else:
    print("il bilgisi doğru değil")

# to use 'or' and 'and'  with if

telefon_markaları={"apple","samsung","huawei","xiaomi"}

if "apple" in telefon_markaları and "samsung" in telefon_markaları and "huawei" in telefon_markaları and "xiamoi":
    print("Eksik Marka Yok")

else :
    print("Eksik Marka Var")



gezi_list=["serhat","aslı","leyla"]

if "serhat" in gezi_list:
    print("serhat geziye katıldı")