import random

bilangan = [
    12, 45, 67, 89, 23, 50, 72, 91, 36, 48,
    9, 33, 75, 81, 29, 56, 42, 60, 87, 19,
    3, 20, 40, 58, 77, 64, 28, 11, 54, 73,
    99, 26, 18, 35, 43, 78, 90, 84, 70, 31,
    5, 13, 22, 47, 63, 85, 94, 68, 39, 6
]
random.seed(40)
random.shuffle(bilangan)

def naive_bayes_sederhana(bilangan, ambang=50):
    total_bilangan = len(bilangan)
    
    prob_kategori1 = len([x for x in bilangan if x <= ambang]) / total_bilangan
    prob_kategori2 = len([x for x in bilangan if x > ambang]) / total_bilangan
    
    kategori = ["Kategori 1" if x <= ambang else "Kategori 2" for x in bilangan]
    
    return kategori, prob_kategori1, prob_kategori2

hasil_kategori, probabilitas_k1, probabilitas_k2 = naive_bayes_sederhana(bilangan)

print("Hasil Klasifikasi Naive Bayes:")
print("Bilangan setelah diacak:", bilangan)
print("Kategori:", hasil_kategori)
print("Probabilitas Kategori 1 (<= 50):", probabilitas_k1)
print("Probabilitas Kategori 2 (> 50):", probabilitas_k2)
