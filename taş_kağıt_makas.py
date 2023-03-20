import random

BilgisayarSkor=0
SizinSkorunuz=0


while True:
    gamer=int(input("""
HOŞGELDİNİZ
1-Taş
2-Kağıt
3-Makas

    Lütfen birini seçiniz\n
                  """))

    pc=random.randint(1,3)
    print(pc)
    if gamer==pc:
        print("Aynı seçimi yaptınız")

    if gamer==1 and pc==2:
        print("Bilgisayar: Kağıt \nBilgisayar Kazandı\n")
        BilgisayarSkor=BilgisayarSkor+10
        print("BilgisayarSkor:{} \nSizin Skorunuz:{}\n".format(BilgisayarSkor,SizinSkorunuz))

    if gamer==1 and pc==3:
       print("Bilgisayar: Makas \nSiz Kazandınız\n")
       SizinSkorunuz=SizinSkorunuz+10
       print("BilgisayarSkor:{} \nSizin Skorunuz:{}\n".format(BilgisayarSkor,SizinSkorunuz))

    if gamer==2 and pc==1:
        print("Bilgisayar: Taş \nSiz Kazandınız\n")
        SizinSkorunuz=SizinSkorunuz+10
        print("BilgisayarSkor:{} \nSizin Skorunuz:{}\n".format(BilgisayarSkor,SizinSkorunuz))
    
    if gamer==2 and pc==3:
        print("Bilgisayar: Makas \nBilgisayar Kazandı\n")
        BilgisayarSkor=BilgisayarSkor+10
        print("BilgisayarSkor:{} \nSizin Skorunuz:{}\n".format(BilgisayarSkor,SizinSkorunuz))

    if gamer==3 and pc==2:
        print("Bilgisayar: Kağıt \nSiz Kazandınız\n")
        SizinSkorunuz=SizinSkorunuz+10
        print("BilgisayarSkor:{} \nSizin Skorunuz:{}\n".format(BilgisayarSkor,SizinSkorunuz))

    if gamer==3 and pc==1:
        print("Bilgisayar: Taş \nBilgisayar Kazandı\n")
        BilgisayarSkor=BilgisayarSkor+10
        print("BilgisayarSkor:{} \nSizin Skorunuz:{}\n".format(BilgisayarSkor,SizinSkorunuz))

    soru=int(input("Oyunu Bitirmek için 0'a \n Devam Etmek İçin 9'a basınız "))

    if soru==0:
        break

    
