not1=int(input("Birinci Sınav Notunu Giriniz: "))
if(not1<0 or not1>100):
    print("Sınav Notunuzu 0-100 Aralığında Girmelisiniz!")
else:
    not2=int(input("İkinci Sınav Notunuzu Giriniz: "))
    if(not2<0 or not2>100):
        print("Sınav Notunuzu 0-100 Aralığında Girmelisiniz!")
    else:
        ortalama=(not1+not2)/2
        print("Ortalamanız: %s"%(ortalama))