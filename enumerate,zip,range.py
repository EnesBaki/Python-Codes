###range
print(list(range(5)))
print([*range(5)])
print(list(range(5,12,2)))

bir5list=list(range(5))
print(bir5list)

for sayi in range(5):
    print(sayi)


###enumarate 

first5inclass=["Aslı","Fatih","Selin","Ali","Neriman"]

for öğrenci in first5inclass:
    print(öğrenci)

for öğrenci in enumerate(first5inclass):
    print(öğrenci)

for index,öğrenci in enumerate(first5inclass):
    print("{}.Öğrenci:{}".format(index+1,öğrenci))


###zip
city=["Sakarya","Kahramanmaraş","Bursa","Amasya","Giresun"]
meşhur=["Islama Köfte","Dondurma","İskender Kebap","Elma","Fındık"]

print("SIRA    ŞEHİR \t         YEMEK")

for sıra,(şehir,yemek) in enumerate(zip(city,meşhur)):
    print(sıra+1,şehir,"\t",yemek)  