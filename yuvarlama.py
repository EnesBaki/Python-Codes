

def tam_sayiya_yuvarla():
    while True:
        girdi=input("ondalık sayı giriniz")
        try:
            girdi=float(girdi)
            print("yuvarlama işlemi sonucu {}".format(round(girdi)))
            status="basarili"
            break
        except :
             print("{} girdisi ondalık sayıya çevrilemiyor".format(girdi))
             status="basarisiz"
             pass
        
        finally:
             print("tam sayıya döndürme işlemi {} olarak tamamlandı".format(status))

tam_sayiya_yuvarla()