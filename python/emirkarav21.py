f1=[]
f2=[]
f3=[]
f4=[]
f5=[]
kalanlar=[]
while True:
    a=input("isminizi giriniz ")
    x=int(input("not giriniz "))
    z=input("")

    if z != "y" :
            if a.isalpha()and x>0:
      
                if 100>=x>=80:
                    f1.append(a)
                    print("F1 SINIF ")
                    
                elif 80>x>=60:
                    f2.append(a)
                    print("F2 SINIF ")
                    
                elif 60>x>=40:
                    f3.append(a)
                    print("F3 SINIF ")
                    
                elif 40>x>=20:
                    f4.append(a)
                    print("F4 SINIF ")
                    
                elif 20>x>=5:
                    f5.append(a)
                    print("F5 SINIF ")
            
                else:
                    kalanlar.append(a)
                    print("KALDI")
            else:
                print("lütfen girdiğiniz değerleri kontrol ediniz.")
    else:
            print(f1,f2,f3,f4,kalanlar)
    
        

