import time

class BasitRNG:
    def __init__(self, tohum=None):
        """
        LCG Algoritması için sabitler.
        Bu değerler genelde yaygın kullanılan standart değerlerdir.
        """
        self.m = 2**31 - 1  # Modulus (büyük bir asal sayı seçtik)
        self.a = 1103515245 # Çarpan
        self.c = 12345      # Artış miktarı
        
        # Eğer tohum (seed) verilmezse o anki zamanı kullanıyoruz ki
        # her çalıştırdığımızda farklı sayılar gelsin.
        if tohum is None:
            self.state = int(time.time())
        else:
            self.state = tohum

    def rastgele_uret(self, min_deger=0, max_deger=100):
        # LCG Formülü: X_(n+1) = (a * X_n + c) % m
        self.state = (self.a * self.state + self.c) % self.m
        
        # Çıkan sayıyı istediğimiz aralığa (min-max) sığdırma işlemi
        aralik = max_deger - min_deger + 1
        sonuc = min_deger + (self.state % aralik)
        
        return sonuc

# Kodu test etmek için basit bir menü
if __name__ == "__main__":
    print("--- Rastgele Sayı Üreteci (LCG) ---")
    
    adet = int(input("Kaç tane sayı üretilsin?: "))
    alt_sinir = int(input("Alt sınır kaç olsun?: "))
    ust_sinir = int(input("Üst sınır kaç olsun?: "))
    
    generator = BasitRNG() # Zamanı seed olarak alır
    
    print("\nÜretilen Sayılar:")
    for i in range(adet):
        sayi = generator.rastgele_uret(alt_sinir, ust_sinir)
        print(f"{i+1}. Sayı: {sayi}")
        
    print("\nİşlem tamamlandı.")