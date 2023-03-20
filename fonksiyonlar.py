
def yas_söyle(x):
    print("Yasınız:{}".format(x))

a=int(input("Yasınız Giriniz \n"))

yas_söyle(a)

###
def ehliyet_durumu_yazdır(**kwargs):
    if "ehliyetdurumu" in kwargs:
        print("ehliyet durumu:{}".format(kwargs["ehliyetdurumu"]))
     
    else:
        pass


ehliyet_durumu_yazdır(ad="enes",okul="btü",il="sakarya",ehliyetdurumu="var")

###

def ogrenci_no_olustur(girişyıl,fakülteno,bölümno,sınıfsıralaması):
    print(girişyıl+fakülteno+bölümno+sınıfsıralaması)


ogrenci_no_olustur("78","45","65","45")


###

def numara_yap(k,l,m,n):
   print("".join([k,l,m,n])) 
    

numara_yap("8","9","9","6")

###
def numara_yap(*args):
   print("".join(args)) 
    

numara_yap("89","9","6")
