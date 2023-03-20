class phonefeatures():
    def __init__(self,brand,camera,pricebuy,memory,modelname) :
        self.brand=brand
        self.camera=camera
        self.pricebuy=pricebuy
        self.memory=memory
        self.modelname=modelname

    

    def pricesellcalculator(self):
        psell=((self.pricebuy*20)/100)+self.pricebuy
        print("{} {} satış fiyatı:{}".format(self.brand,self.modelname,psell))
    

phone1=phonefeatures("ıPHONE","16 MP",5000,"128 GB","8 PLUS")
phone2=phonefeatures("Samsung","24 MP",3500,"128 GB","A90")

phone1.pricesellcalculator()
phone2.pricesellcalculator()

