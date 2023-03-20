
def daire_alan(r):
    pi=22/7
    alan=pi*r*r
    print("Daire Alanı:{}".format(alan))

print("Daire alanı hesaplama programramına hoşgeldiniz!")
a= float(input("Lütfen alanı bulmak istediğiniz dairenin yarıçapını giriniz\n"))

daire_alan(a)


def asal_test(sayi):
    a=2
    while a<sayi:
        if sayi/a==0:
            print("asal değil")
        else:
            a=a+1
            
print("asal sayi")  

asal_test(9)