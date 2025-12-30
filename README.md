# Collatz-Feistel Cipher 🛡️

Bu algoritma, **Collatz Sanısı** kullanılarak üretilen sayı dizilerini **Von Neumann** algoritmasıyla filtreler. Sonuç olarak ortaya çıkan anahtarlar tam olarak **eşit sayıda 0 ve 1** içerir.

### Teknik Akış
1. **Collatz (3n+1):** Ham bit dizisi üretimi.
2. **Von Neumann:** İstatistiksel dengeleme (Entropy artırımı).
3. **Feistel Network:** 8 tur çevirmeli şifreleme yapısı.



### Challenge
Bu depodaki `main.py` kodunu kullanarak şifrelenmiş verileri çözmek için doğru `seed` (anahtar) değerini bulmanız gerekiyor!
