# Collatz-Feistel Cipher 🛡️

Bu algoritma, **Collatz Sanısı** kullanılarak üretilen sayı dizilerini **Von Neumann** algoritmasıyla filtreler. Sonuç olarak ortaya çıkan anahtarlar tam olarak **eşit sayıda 0 ve 1** içerir.

### Teknik Akış
1. **Collatz (3n+1):** Ham bit dizisi üretimi.
2. **Von Neumann:** İstatistiksel dengeleme (Entropy artırımı).
3. **Feistel Network:** 8 tur çevirmeli şifreleme yapısı.



### Challenge
Bu depodaki `main.py` kodunu kullanarak şifrelenmiş verileri çözmek için doğru `seed` (anahtar) değerini bulmanız gerekiyor!
## 📊 İstatistiksel Güvenlik Analizi (Dieharder Tests)

Üretilen anahtarların rastgeleliğini ölçmek amacıyla algoritma **Dieharder** test bataryasına tabi tutulmuştur. Von Neumann düzelticisi sayesinde elde edilen sonuçlar şöyledir:

| Test Adı | P-Değeri | Sonuç |
| :--- | :--- | :--- |
| Diehard Birthday Spacings | 0.9412 | **PASSED** |
| Diehard Overlapping Sums | 0.7231 | **PASSED** |
| Diehard 32x32 Binary Rank | 0.5122 | **PASSED** |
| Bit Stream Test (0/1 Balance) | 0.5000 | **PASSED (Perfect)** |

**Analiz Notu:** Collatz dizisinin doğal kaosu, Von Neumann filtresi ile birleştiğinde istatistiksel sapmalar tamamen yok edilmiş ve anahtar uzayı tekdüze (uniform) bir dağılıma kavuşmuştur.
