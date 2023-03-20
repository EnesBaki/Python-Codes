def kare_al(x):
    print(x**2)

## map bir işlemin listedeki tüm elemanlar uygulanmasını sağlar 
## range gibi listeye atanarak kullanılır

ilk10list=list(range(1,11))
[*map(kare_al,ilk10list)]

print(ilk10list)


## filter 

def cift_sayi_filtrele(sayi):                      
    if sayi%2==0:
        print(sayi)

def cift_sayi_filtrele2(x):
    print(x) if x%2==0 else None       #filtreleme
     

cift_sayi_filtrele2(5)

list(filter(cift_sayi_filtrele,ilk10list))

##lambda fonksiyonu tanıtmadan yol üstünde işlem yapmasını sağlar

sayilar=[1,2,3,4,5,6,7,8,9]

alist=list(map(lambda x:x**2 ,sayilar))
print(alist)

ciftlist=list(filter(lambda x:x if x%2==0 else None,sayilar))
print(ciftlist)
