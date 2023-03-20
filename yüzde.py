print("Faiz Hesaplama Programına Hoşgeliniz")
isim= input("isminizi giriniz")

print("{} Bey Hoşgeldiniz".format(isim))

kreditutar=int(input("Çekmek istediğiniz Kredi Tutarını Giriniz\n"))

faiz=(kreditutar*8)/100

toplamödenecek=faiz+kreditutar

print("Toplam faiz:{}".format(faiz))
print("Toplam Ödenecek:{}".format(toplamödenecek))
