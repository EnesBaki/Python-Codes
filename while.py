print("Faktoriyeli Hesaplanacak Sayi gir")
a=int(input("Girdiğiniz Sayi:"))
print("{}!".format(a))

sayac=1
sonuc=1

while sayac<a:

    sonuc=sonuc*sayac
    sayac+=1

print("{}!={}".format(a,sonuc))


a="sd"
print(type(a))