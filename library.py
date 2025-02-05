"""
Kütüphane Yönetim Sistemi (Encapsulation, Composition, Exception Handling)
Bu projede bir kütüphane sistemini modelleyeceğiz.
Şartlar:
Kitap sınıfı:
Kitap adı, yazar, sayfa sayısı, ISBN bilgilerini içermeli.
Kutuphane sınıfı:
Kitap ekleme (kitap_ekle(kitap)), 
kitap kaldırma (kitap_sil(isbn)), 
tüm kitapları gösterme (kitaplari_goster()) metodları olmalı.
Exception Handling (Hata Yakalama): Bir kitap zaten ekliyse hata fırlatmalı."""


class Kitap:
    def __init__(self, kitap_adi, yazar_adi, sayfa_sayisi, isbn):
        self.kitap_adi = kitap_adi
        self.yazar_adi = yazar_adi
        self.sayfa_sayisi = sayfa_sayisi
        self.isbn = isbn

class Kutuphane:
    def __init__(self):
        self.kitaplar = {}


    def kitap_ekle(self, kitap):
        try:
            if kitap.isbn in self.kitaplar:
                raise Exception("Bu kitap zaten kütüphaneye eklenmiş.")
            
            self.kitaplar[kitap.isbn] = kitap
            print(f"""
            Kitap kütüphaneye eklendi:      
            Kitap Adı :{kitap.kitap_adi}
            Yazar Adı :{kitap.yazar_adi}
            Sayfa Sayısı :{kitap.sayfa_sayisi}
            ISBN :{kitap.isbn}""")
        
        except Exception as e:
            print(f"Hata : {e}")


    def kitap_sil(self, isbn):
        if isbn in self.kitaplar:
            silinen_kitap = self.kitaplar.pop(isbn)
            print(f""" Kitap kütüphaneden silindi:   
            Kitap Adı :{silinen_kitap.kitap_adi}
            Yazar Adı :{silinen_kitap.yazar_adi}
            Sayfa Sayısı :{silinen_kitap.sayfa_sayisi}
            ISBN :{silinen_kitap.isbn}""")
        


    def kitaplari_goster(self):
        for kitap in self.kitaplar.values():
            print(f"""
            Kitap Adı: {kitap.kitap_adi}
            Yazar: {kitap.yazar_adi}
            Sayfa Sayısı: {kitap.sayfa_sayisi}
            ISBN: {kitap.isbn}""")
            
        
        
kitap1 = Kitap("Kızıl Veba", "Jack London", 328, "123456789")
kitap2 = Kitap("Siyah Gözler", "Cemil Süleyman", 152, "987654321")

kutuphane = Kutuphane()

kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)

kutuphane.kitap_ekle(kitap1)

kutuphane.kitaplari_goster()

kutuphane.kitap_sil("123456789")

kutuphane.kitaplari_goster()

 