
class seyahat():
    
    def __init__(self,kod,yolcusayısı,koltuksayısı):
        self.kod=kod
        self.yolcusasayısı=yolcusayısı
        self.koltuksayısı=koltuksayısı
        
    def seyahat_info(self):
        print("{} numaralı seyahat kayıtlarımızda mevcuttur.".format(self.kod))


class otobus(seyahat):

    def __init__(self, kod, yolcusayısı, koltuksayısı,kalkış,varış,duraklar,plaka):
        super().__init__(kod, yolcusayısı, koltuksayısı)
        self.kalkış=kalkış
        self.varış=varış
        self.duraklar=duraklar
        self.plaka=plaka
    
    def oto_info(self):
        print("{} plakalı otobüs seyahate hazırdır.\n".format(self.plaka))

class uçak(seyahat):
    def __init__(self, kod, yolcusayısı, koltuksayısı,kalkış,varış,uçaktipi):
        super().__init__(kod, yolcusayısı, koltuksayısı)
        self.kalkış=kalkış
        self.varış=varış
        self.uçaktipi=uçaktipi
    
    def uçak_info(self):
        print("{} tipli seyahat uçağımız sefere hazırdır.\n".format(self.uçaktipi))

class tren(seyahat):
    def __init__(self, kod, yolcusayısı, koltuksayısı,kalkış,varış,vagonsayısı):
        super().__init__(kod, yolcusayısı, koltuksayısı)
        self.kalkış=kalkış
        self.varış=varış
        self.vagonsayısı=vagonsayısı
    
    def tren_info(self):
        print("{} vagon sayılı tren sefer için hazırdır \n".format(self.vagonsayısı))

    
bus1=otobus(100,50,90,"Sakarya","Bursa",["Kocaeli","Yalova"],"54 SB 011")
plane1=uçak(101,100,200,"IST","BOD","S11")
train1=tren(102,80,80,"ADP","BSTNC",8)

bus1.seyahat_info()
bus1.oto_info()

plane1.seyahat_info()
plane1.uçak_info()

train1.seyahat_info()
train1.tren_info()
