


def selamsöyle():
    print("Selam, nasılsın?")

selamyaz=selamsöyle

selamyaz()


def deco(a):

   def wrapper():
    print("çalışma başladı")

    a()

    print("çalışma bitti")
   
   return wrapper



def helloyaz():
    print("hello")


helloyaz=deco(helloyaz)
helloyaz()



def deco(func):
    def wrapper():
        
        print("Birazdan gönderilen fonksiyon işlenecek")

        func()

        print("Gönderilen fonksiyon işlendi")

    return wrapper



def bilgi_ver():
    print("Sakarya ilinin plaka kodu 54'tür ")


bilgi_ver=deco(bilgi_ver)

bilgi_ver()
