import datetime 
import time


bugün=datetime.date.today()

print(bugün)
 
dün=datetime.date(2022,8,16)

print(dün)

print(bugün - dün)

yarın= datetime.timedelta(days=1) + bugün

print(yarın)

a=datetime.date.isocalendar(bugün) #saymaya 1 den başlar
print(a)

b=datetime.date.weekday(bugün)     #saymaya 0 dan başlar 0 pazartesi 1 salı
print(b)

zaman=datetime.time(21,10,7)
print(zaman,zaman.hour,zaman.minute,zaman.second)


doğum_günüm=datetime.datetime(2002,3,4,11,00)
print(doğum_günüm)

print(time.time()) #60 lara bölündükçe saat dakika gibi verilere ulaşılablir