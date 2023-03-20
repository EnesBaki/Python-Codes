import random
 
a=random.random()   # 0-1 arası sayı tutar
print(a)

b=random.uniform(2,10)  #2-10 arası sayı tutar 
print(b)

c=random.randint(1,100) #1-100 arası int sayı tutar
print(c)

e=list(range(1,11))

print(random.choice(e))

print(random.sample(range(1,11),k=3))

listA=[1,2,3,4,5,6,7,8,9]
print(listA)

random.shuffle(listA)
print(listA)