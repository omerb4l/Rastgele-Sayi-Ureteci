## Rapor

Bu projede rastgele sayı üretmek için **Linear Congruential Generator (LCG)** yöntemini seçtim. Seçmemin nedeni, bu algoritmanın bilgisayar bilimleri tarihindeki en eski ve en bilinen yöntemlerden biri olması. Ayrıca kodlaması sade olduğu için çalışma mantığını takip etmek çok daha kolay.


### Nasıl Çalışıyor?

Bilgisayarların kendi kendine "aklından sayı tutması" imkansız olduğu için, aslında matematiksel bir formül kullanarak sayıları karıştırıyoruz. Buna "Sözde Rastgelelik" (Pseudo-Random) deniyor. 

Kullandığım temel formül şu:

`X_yeni = (a * X_eski + c) % m`

Buradaki mantığı şöyle özetleyebilirim:
1.  **Başlangıç (Seed):** Kod ilk çalıştığında bir başlangıç sayısına ihtiyaç duyar. Ben bunun için o anki **sistem saatini (time)** kullandım. Çünkü zaman sürekli değiştiği için her çalıştırdığımızda farklı sayılar elde ediyoruz.
2.  **İşlem:** Elimizdeki sayıyı belirli bir sayıyla çarpıp ($a$), üzerine başka bir sayı ekliyoruz ($c$).
3.  **Sınırlama (Mod):** Sonucun çok büyümemesi ve istediğimiz aralıkta kalması için mod alma işlemi ($m$) uyguluyoruz. Kalan sayı, bizim yeni rastgele sayımız oluyor.

Kodumda kullandığım $a, c$ ve $m$ değerlerini kafama göre seçmedim; bunlar POSIX standartlarında önerilen ve sayıların tekrar etme süresini uzatan yaygın değerler.

### Güvenlik Analizi

Bu algoritma **hızlıdır** ancak **kriptografik olarak güvenli değildir.** Mantığı doğrusal olduğu için, eğer kötü niyetli biri kodumda kullandığım sabit sayıları (çarpan ve artış miktarını) öğrenirse ve üretilen birkaç sayıyı takip ederse, bir sonraki gelecek sayıyı matematiksel olarak hesaplayabilir.

Bu yüzden LCG algoritması; bankacılık işlemleri veya şifre üretimi gibi yüksek güvenlik gerektiren yerlerde **kullanılmamalıdır**.
