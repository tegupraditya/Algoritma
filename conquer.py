import random

bilangan = [
    12, 45, 67, 89, 23, 50, 72, 96, 36, 48,
    9, 33, 75, 81, 29, 56, 42, 60, 87, 19,
    3, 20, 40, 58, 77, 64, 28, 11, 54, 73,
    99, 26, 18, 35, 43, 78, 90, 84, 70, 31,
    5, 13, 22, 47, 63, 85, 94, 68, 39, 6
]
random.seed(40)
random.shuffle(bilangan)

def cari_maksimum(bilangan):
    if len(bilangan) == 1:
        return bilangan[0]
    
    tengah = len(bilangan) // 2
    maksimum_kiri = cari_maksimum(bilangan[:tengah])
    maksimum_kanan = cari_maksimum(bilangan[tengah:])
    return max(maksimum_kiri, maksimum_kanan)

bilangan_maksimum = cari_maksimum(bilangan)

print("Daftar bilangan setelah diacak:", bilangan)
print("Bilangan maksimum (Divide and Conquer):", bilangan_maksimum)
