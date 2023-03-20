yorum_yapanlar=["ismail","aslı","mehmet","ezgi","kenan"]

for kullanici in yorum_yapanlar:
    print(kullanici)


kullanici_sayisi=0
print("kullanici sayisi \t kullanici ismi ")
for kullanici in yorum_yapanlar:
    kullanici_sayisi=kullanici_sayisi+1
    print( kullanici_sayisi,"\t \t \t", kullanici)

#### trying something

yorum_yapanlar=["ismail demir","aslı demir ","mehmet demir","ezgi demir ","kenan demir"]
kullanicisayisi=0
for kullanici in yorum_yapanlar:
    kullanicisayisi=kullanicisayisi+1
    ad=kullanici.split()[0]
    soyad=kullanici.split()[1]
    print("{}.kullanici".format(kullanicisayisi),"kullanicinin adi {}".format(ad),"kullanicinin soyadi {}".format(soyad))

###liste içi liste

küme1=[[1,2,7],[9,6,7],[7,8,10]]

for x,y,z in küme1:
    print(x,y,z)



##for ve dictionary

ogrenci={ "name":"john",
          "number":594,
          "class":11,
          "branch":"C"}

for k,v in ogrenci.items():
    print("key:{} \t value:{}".format(k,v))