def asalmı(sayi):
    i=2
    while i<=sayi:
        if sayi==2:
            print("asal değil")
            i=i+1
            break
        elif sayi%i==0:
            print("asal değil")
            break
        else:
            i=i+1
    while i==sayi:
        print("asaldır")
        break


a=int(input("Asallığı test edilecek sayı gir"))

asalmı(a)

def strfilter(list_a):
    for index in list_a:
        if type(index)== str :
            print(index)
            
        else :
            pass


a={"sdd","sdş",84,14,4.84,"sx"}

strfilter(a)


