from collections import Counter
import random

list1=random.sample(range(1,11),k=4)
list2=random.sample(range(1,11),k=4)
list3=random.sample(range(1,11),k=4)
list4=random.sample(range(1,11),k=4)

liste_listesi=[list1,list2,list3,list4]
liste_toplam=list1+list2+list3+list4

print(Counter(liste_toplam))

sarki= """Yine bana gel\n
          Yana yana yine beni sev\n
          Yine bana gel\n
          Yana yana yine beni sev"""

print(Counter(sarki.lower().split()))
print(Counter(sarki.lower().split()).most_common(1))
print(Counter(sarki.lower().split()).most_common(2))
