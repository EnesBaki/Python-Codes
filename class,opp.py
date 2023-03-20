class ucuslar():
    firma="THY"

    def __init__(self,saat,süre,nereden,nereye,kapasite,yolcu):
        self.saat=saat
        self.süre=süre
        self.nereden=nereden
        self.nereye=nereye
        self.kapasite=kapasite
        self.yolcu=yolcu
    
    def __repr__(self) :  ##ucus1 print yaptırıldığında çalışan kod yazılır 
      return "{} kalkış saatli sefer sistemde mevcuttur.".format(self.saat)

    def anons_yap(self):
        print("{} kalkışlı {} varışlı uçağımız kalkış yapmıştır. Yolcuğumuz {} dakika sürecektir".format(self.nereden,self.nereye,self.süre))


    def koltuksayigüncel(self):
        return self.kapasite-self.yolcu

ucus1=ucuslar("15.00",120,"sakarya","antalya",250,240)


ucus1.anons_yap()
print(ucus1.koltuksayigüncel())
print(ucus1.yolcu)
print(ucus1)