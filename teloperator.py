import re
def operator_bul(num):
    pattern1="054\d{8}"
    pattern2="053\d{8}"
    pattern3="050\d{8}"

    try:
       if re.search(pattern1,num).group()==num:
        print("OPERATOR:VODAFONE")
    
    except:
        pass
        
    
    
    try:
       if re.search(pattern2,num).group()==num:
        print("OPERATOR:TURKCELL")
    
    except:
        pass



    try:
       if re.search(pattern3,num).group()==num:
        print("OPERATOR:TURK TELEKOM")
    
    except:
        pass


      
a=input(str("Bir telefon numarası giriniz\n"))
operator_bul(a)

num="05415180229"
pattern1="054\d{8}"
re.search(pattern1,num)