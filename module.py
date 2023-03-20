import os                                    #os kütüphanesini ekler
print(os.getcwd())                           # mevcut dosyanın path'ı nı gösterir
print(os.listdir())                          # mevcut dosyanın bulunduğu klasördeki diğer dosyaları gösterir
print(os.listdir("C:\\Users\Blue\Desktop"))  # içinde yazılan adresteki klasörleri listeler "C:\\" şeklinde başlanmalıdır

## os.listdir komutu default olarak aktif olarak kod yazılan dosyanın pathini gösterir.
## ıf we want to change the default argument, we should use "os.chdir()"

os.chdir("C:\\Users\Blue\Desktop\p9")
print(os.listdir())

os.mkdir("C:\\Users\Blue\Desktop\PythonKlasör") #klasör oluşturur
os.rmdir("C:\\Users\Blue\Desktop\PythonKlasör") #klasör siler

#klasör içinde dosya oluşrturmak,dosyaya yazı eklemek
  
   ## os.O_RDONLY
   ## os.O_WRONLY
   ## os.O_RDWR
   ## os.O_CREAT
   ## os.O_RDWR |os.O_CREAT  2 özellik isteniyorsa | işareti araya konulur

trytext= os.open("deneme_metin.txt",os.O_RDWR |os.O_CREAT )
os.write(trytext,"Dosya olusturdum ve icine bunu yazdim :). Türkçe kontrol".encode())
os.close(trytext)

trytext=os.open("deneme_metin.txt",os.O_RDONLY)
icerik=os.read(trytext,5 ) ## ilk 5 karakteri okur

print(icerik)

##metin içerisindeki tüm karakterleri yazdırmak için için öncelkle stat komutu kullanarak metnin kaç karakterden oluştuğunu öğreniyoruz.

print(os.stat(trytext))

uzunluk=os.stat(trytext).st_size
trytext=os.open("deneme_metin.txt",os.O_RDONLY)
icerik=os.read(trytext,uzunluk) ## tüm karakterleri okudu
print(icerik.decode())

##  os.unlink("deneme_metin.txt") ##dosya siler

##os.mkdir("filecre78d")
##os.rename("filecre78d","newnamefile") #dosya adını değiştirir

a=os.open("okubnu.txt",os.O_RDONLY)
yazi=os.read("okubnu.txt",5)
print(yazi)
