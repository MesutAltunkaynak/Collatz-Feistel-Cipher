import struct

class CollatzFeistel:
    def __init__(self, seed):
        self.seed = seed

    def _get_balanced_bits(self, seed_val, length):
        """Collatz + Von Neumann Düzeltici: Eşit sayıda 0 ve 1 garantisi"""
        raw_bits = []
        curr = seed_val
        while len(raw_bits) < length * 10:
            if curr % 2 == 0:
                curr //= 2
                raw_bits.append(0)
            else:
                curr = 3 * curr + 1
                raw_bits.append(1)
            if curr <= 1: curr = seed_val + len(raw_bits) + 17
        
        balanced = []
        for i in range(0, len(raw_bits)-1, 2):
            pair = raw_bits[i:i+2]
            if pair == [0, 1]: balanced.append(0)
            elif pair == [1, 0]: balanced.append(1)
            if len(balanced) == length: break
        return balanced

    def encrypt_block(self, block_64bit):
        L = (block_64bit >> 32) & 0xFFFFFFFF
        R = block_64bit & 0xFFFFFFFF
        for i in range(8):
            bits = self._get_balanced_bits(self.seed + i, 32)
            round_key = 0
            for b in bits: round_key = (round_key << 1) | b
            L, R = R, L ^ (R ^ round_key)
        return (L << 32) | R

if __name__ == "__main__":
    cf = CollatzFeistel(seed=12345)
    print(f"Şifreli: {hex(cf.encrypt_block(0xABCDEFFF12345678))}")
