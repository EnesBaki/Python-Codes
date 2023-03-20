

print('Hi,George \n its  a new line\tspacee   ')
print(5)
a=5
b=3
print(a*3)

print("my name is {0}, I am {1}.".format("Enes Baki",19))
print("My hometown is {city} in {country}".format(city="Sakarya",country="Türkiye")) 

list_a=[1,"tea",2,False,1]
set_a={1,"tea",2,False}
dict_a= {"name":"Enes", "age":19}
tup_a=( 1,2,"textfalanfilan") #cannot use delete or add operator

print(dict_a["age"])

#string ifadesindeki bazı opsiyonlar

team = "galatasaray"
print(team)
print(team[2])
print(team[2:7])

print(team.upper())  #büyük yazar
print(team.lower())  #küçük yazar
print(team.split())  #ayırma
print(team.split("a"))

#Liste özellikleri

list1 =["z","z","b","c","e","f","g"]

list1.append("d")  #listeye yeni eleman ekler
print(list1)

list1.pop()  #listedeki son elemanı atar
print(list1)

list1.pop(5) #5. indexteki elemanı atar
print(list1)

list1.sort() #listedeki elemanları sıralar
print(list1)

list1.reverse() #ters çevirir

list1.count("z")

set(list1)  #liste olan list1'i set veri tipine dönüştürür
