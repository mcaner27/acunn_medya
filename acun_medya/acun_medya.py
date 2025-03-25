def merhaba_de():
    print("Merhaba, Python!")

merhaba_de()

#2.Isim ve Soyisim Yazdiran Fonksiyon
def tam_ad_yazdir():
    isim = input("Isminizi girin: ")
    soyisim = input("Soyisminizi girin: ")
    print(f"{isim} {soyisim}")

tam_ad_yazdir()

#3.Listeden Tek Sayilari Bulan Fonksiyon
def tek_sayilari_bul(liste):
    return [sayi for sayi in liste if sayi % 2 != 0]

sayilar = list(map(int, input("Liste icin sayilari girin (virgulle ayirin): ").split(',')))
print("Tek sayilar:", tek_sayilari_bul(sayilar))

#4.Dort islem Yapan Fonksiyonlar
def topla():
    sayi1 = int(input("Birinci sayiyi girin: "))
    sayi2 = int(input("Ikinci sayiyi girin: "))
    return sayi1 + sayi2

print("Toplam:", topla())


def bolme():
    sayi1 = int(input("Bolunen sayiyi girin: "))
    sayi2 = int(input("Bolen sayiyi girin: "))
    return "Bolen kisim 0 olamaz" if sayi2 == 0 else sayi1 / sayi2

print("Bolme:", bolme())

def carpma():
    sayi1 = int(input("Birinci sayiyi girin: "))
    sayi2 = int(input("Ikinci sayiyi girin: "))
    return sayi1 * sayi2

print("Carpma:", carpma())


def cikarma():
    sayi1 = int(input("Birinci sayiyi girin: "))
    sayi2 = int(input("Ikinci sayiyi girin: "))
    return sayi1 - sayi2

print("Cikarma:", cikarma())


def mod():
    sayi1 = int(input("Birinci sayiyi girin: "))
    sayi2 = int(input("Ikinci sayiyi girin: "))
    return sayi1 % sayi2

print("Mod:", mod())
#5.Metin Uzerinde Farkli islemler Yapan Fonksiyon

def metin_islem():
    metin = input("Metni girin: ")
    islem_tipi = input("Islem tipini girin (ters, buyuk, kucuk, uzunluk): ")
    if islem_tipi == "ters":
        return metin[::-1]
    elif islem_tipi == "buyuk":
        return metin.upper()
    elif islem_tipi == "kucuk":
        return metin.lower()
    elif islem_tipi == "uzunluk":
        return len(metin)
    else:
        return "Gecersiz islem"

print("Sonuc:", metin_islem())
#6.Birden Fazla isim Ekleyen Fonksiyon
isimler = []

def isim_ekle():
    global isimler
    yeni_isimler = input("Eklemek istediginiz isimleri girin (virgulle ayirin): ").split(',')
    isimler.extend(isim.upper() for isim in yeni_isimler)
    return isimler

print("Eklenen isimler:", isim_ekle())
#7.Metindeki Kelime Sayisini Analiz Eden Fonksiyon


def kelime_sayisi(metin):
    return len(metin.split())


def cumle_analiz():
    metin = input("Bir cumle girin: ")
    return "Cumle uzun" if kelime_sayisi(metin) >= 5 else "Cumle kisa"

print("Cumle analizi:", cumle_analiz())

#8.Recursive Toplam Hesaplayan Fonksiyon
def toplam():
    n = int(input("Bir sayi girin: "))
    def hesapla(m):
        if m == 1:
            return 1
        return m + hesapla(m - 1)
    return hesapla(n)

print("Toplam:", toplam())