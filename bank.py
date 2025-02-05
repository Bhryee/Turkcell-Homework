"""
Banka Hesap Yönetimi (Encapsulation, Inheritance, Polymorphism)
Bu projede, banka hesapları için bir sistem oluşturacağız.

Şartlar:
Hesap sınıfı:
Hesap sahibinin adı, hesap numarası, bakiye bilgilerini içermeli.

para_yatir(miktar), para_cek(miktar), bakiye_goster() metodları olmalı.

Encapsulation uygulanmalı (__bakiye private olmalı).

VadesizHesap ve VadeliHesap sınıfları Hesap sınıfından türetilmeli.

VadeliHesap için faiz hesaplayan faiz_hesapla() metodu eklenmeli.

Polymorphism (Çok Biçimlilik) için para_cek() metodu VadeliHesap içinde özelleştirilmeli.

Inheritance (Miras Alma) ile ortak özellikler Hesap sınıfında tanımlanmalı.
"""


class Hesap:
    def __init__(self, ad, hesap_no, bakiye):
        self.ad = ad
        self.hesap_no = hesap_no
        self.__bakiye = bakiye

    # Getter: Bakiye erişimi
    def get_bakiye(self):
        return self.__bakiye

    # Setter: Bakiye güncelleme
    def set_bakiye(self, miktar):
        self.__bakiye = miktar

    def para_yatir(self, bakiye):
        self.__bakiye += bakiye
        print(f"{self.hesap_no} hesabına {bakiye} tl para yatırıldı.")

    def para_cek(self, bakiye):
        self.__bakiye -= bakiye
        print(f"{self.hesap_no} hesabından {bakiye} tl para çekildi.")

    def bakiye_goster(self):
        print(f"Toplam bakiye : {self.__bakiye} tl.")


class VadesizHesap(Hesap):
    pass

class VadeliHesap(Hesap):
    def __init__(self,ad, hesap_no, bakiye, faiz_orani):
        super().__init__(ad, hesap_no, bakiye)
        self.faiz_orani = faiz_orani

    def faiz_hesapla(self):
        faiz = self.get_bakiye() * (self.faiz_orani / 100)
        return faiz

    def para_cek(self, bakiye):
        faiz = self.faiz_hesapla()
        toplam_bakiye = self.get_bakiye() + faiz
        print(f"{self.hesap_no} hesabından {bakiye} tl para çekildi. Faiz dahil toplam bakiye: {toplam_bakiye} tl.")

        
        


hesap1 = Hesap("Ahmet", "12345", 1000)
hesap1.para_yatir(500)  # 500 TL yatırma
hesap1.para_cek(200)  # 200 TL çekme
hesap1.bakiye_goster()

print("\n----- Vadeli Hesap -----")
vadeli_hesap1 = VadeliHesap("Mehmet", "67890", 1000, 5)  # %5 faiz
vadeli_hesap1.para_yatir(500)  # 500 TL yatırma
vadeli_hesap1.para_cek(200)  # Vade bitmeden para çekme (hata verecek)
vadeli_hesap1.bakiye_goster()  # Bakiyeyi gösterme
