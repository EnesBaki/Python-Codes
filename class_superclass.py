
class factoryinpeople():
     
   firma="B Holding"

   def __init__(self,personelid,age,number,job):
    self.personelid=personelid
    self.age=age
    self.number=number
    self.job=job


   def bilgi(self):
    print("{} numaralı çalışanımızın departmanı:{}".format(self.personelid,self.job))




class boardofmanagament(factoryinpeople):
     
    def __init__(self,degree,commission,personelid,age,number,job):
        factoryinpeople.__init__(self,personelid,age,number,job)
        self.degree=degree
        self.commission=commission
        


ali=boardofmanagament("master",1000,99123,22,53546211,"engineer")
print(ali.age)