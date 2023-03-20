

def deco(func):

    def wraper():
        print("İstediğiniz fonksiyon birazdan çalışacak")

        func()

        print("İstediğiniz fonksiyon başarıyla çalıştırıldı")
    
    return wraper


@deco
def bilgiver():
    print("Galatasaray 4 yıldızlı ilk ve tek takımdır")


bilgiver()

##argüman alan fonksiyonlarda decorator
def deco2(fonks):
    def wrapper(*args):

       print("basla")

       fonks(*args)

       print("bitti")

    return wrapper
  
@deco2
def infoyaz(a,b):
    print("toplam: {}".format(a+b))

infoyaz(5,4)

## argüman alan decorator

def deco3(mesaj1,mesaj2):
    def ara_katman(f):
        def wrapper(*args):
            print(mesaj1)

            f(*args)

            print(mesaj2)
    
        return wrapper
    return ara_katman

@deco3("start","finished")
def toplamyaz(a,b):
    print("toplam: {}".format(a+b))

toplamyaz(5,5)



