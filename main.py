# Collatz-Feistel Balanced Cipher Implementation
import struct

class CollatzCipher:
    def __init__(self, seed):
        self.seed = seed

    def generate_balanced_bits(self, seed_val, n_bits):
        """3. ve 4. Yöntemlerin Birleşimi: Von Neumann Düzeltici"""
        bits = []
        curr = seed_val
        while len(bits) < n_bits * 10: # Dengeleme kaybı için fazla üret
            if curr % 2 == 0:
                curr //= 2
                bits.append(0)
            else:
                curr = 3 * curr + 1
                bits.append(1)
            if curr <= 1: curr = seed_val + len(bits) + 13 # Döngü kırıcı
        
        balanced = []
        for i in range(0, len(bits)-1, 2):
            pair = bits[i:i+2]
            if pair == [0, 1]: balanced.append(0)
            elif pair == [1, 0]: balanced.append(1)
            if len(balanced) == n_bits: break
        return balanced

    def feistel_round(self, left, right, round_key):
        # Feistel Tur Fonksiyonu
        temp = right
        f_func = right ^ round_key
        new_right = left ^ f_func
        return temp, new_right

    def process(self, block_64bit, encrypt=True):
        L = (block_64bit >> 32) & 0xFFFFFFFF
        R = block_64bit & 0xFFFFFFFF
        
        # 8 Tur İşleme
        round_keys = [int(''.join(map(str, self.generate_balanced_bits(self.seed + i, 32))), 2) for i in range(8)]
        
        if not encrypt:
            round_keys = round_keys[::-1]

        for r_key in round_keys:
            L, R = self.feistel_round(L, R, r_key)
            
        return (R << 32) | L # Son turda yer değiştirme

# ÖRNEK KULLANIM
if __name__ == "__main__":
    my_seed = 123456789
    cipher = CollatzCipher(my_seed)
    message = 0x1122334455667788
    
    enc = cipher.process(message, encrypt=True)
    dec = cipher.process(enc, encrypt=False)
    
    print(f"Seed: {my_seed}")
    print(f"Orijinal: {hex(message)}")
    print(f"Şifreli:  {hex(enc)}")
    print(f"Çözülen:  {hex(dec)}")

