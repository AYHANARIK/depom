sayi1=int(input("Başlangıç sayısını giriniz: "))
sayi2=int(input("Bitiş sayısını giriniz: "))
toplam=0
for sayilar in range(sayi1,sayi2+1):
    print(sayilar)
    toplam=toplam+sayilar
    print("Sayıların Toplamı: ",toplam)