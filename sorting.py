# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Rekursif memanggil merge_sort
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Menggabungkan kedua bagian
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menyalin elemen yang tersisa
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Data input
X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Menggunakan Merge Sort
sorted_merge = merge_sort(X.copy())
print("Hasil Merge Sort:", sorted_merge)
print("Penjelasan:")
print("Best Case: O(n log n) - Merge Sort memiliki waktu terbaik (best case) sebesar O(n log n), terlepas dari bagaimana data diurutkan. Bahkan jika array sudah sepenuhnya terurut, algoritma tetap harus membagi array menjadi dua bagian, merekursi setiap bagian, dan kemudian menggabungkannya kembali. Proses ini dilakukan secara konsisten, karena Merge Sort bekerja secara independen terhadap urutan data. Oleh karena itu, tidak ada cara untuk mempercepat waktu eksekusi meskipun data sudah dalam kondisi terbaik.")
print("Worst Case: O(n log n) - Dalam kondisi terburuk (worst case), Merge Sort tetap memiliki waktu O(n log n). Tidak seperti Quick Sort, Merge Sort tidak bergantung pada pemilihan elemen pivot atau distribusi data. Semua array, baik yang sudah terurut, terbalik, atau acak, diproses dengan cara yang sama. Proses pembagian array menjadi dua bagian, rekursi, dan penggabungan tetap dilakukan, sehingga waktu eksekusi tidak berubah.")
print("Average Case: O(n log n) - Waktu rata-rata (average case) untuk Merge Sort juga O(n log n). Karena algoritma ini secara rekursif membagi array menjadi dua bagian yang hampir sama besar dan menggabungkannya dengan kompleksitas linear, kinerjanya konsisten untuk data acak. Dengan struktur algoritma yang deterministik, Merge Sort memberikan performa yang dapat diandalkan untuk berbagai jenis input, baik terurut maupun tidak.\n")

# Menggunakan Quick Sort
sorted_quick = quick_sort(X.copy())
print("Hasil Quick Sort:", sorted_quick)
print("Penjelasan:")
print("Best Case: O(n log n) - Waktu terbaik (best case) untuk Quick Sort adalah O(n log n), yang terjadi ketika pivot yang dipilih selalu membagi array menjadi dua bagian yang hampir sama besar. Dalam kondisi ini, kedalaman rekursi berkurang secara optimal, sehingga waktu yang dibutuhkan untuk membagi array dan menyortirnya menjadi minimum. Misalnya, array [4, 2, 6, 3, 5] dengan pivot ideal dapat menghasilkan pembagian yang merata, membuat algoritma sangat efisien.")
print("Worst Case: O(n²) - Kondisi terburuk (worst case) untuk Quick Sort terjadi jika pivot yang dipilih selalu merupakan elemen terkecil atau terbesar, menghasilkan pembagian array yang sangat tidak seimbang. Dalam situasi seperti ini, algoritma menjadi tidak efisien dengan waktu O(n²) karena hanya satu elemen yang diproses di setiap rekursi, sedangkan sisanya tetap berada di subarray besar. Contohnya adalah array [9, 8, 7, 6, 5], jika pivotnya selalu elemen pertama, rekursi akan terus berjalan dengan pembagian yang tidak ideal.")
print("Average Case: O(n log n) -Dalam kondisi rata-rata (average case), Quick Sort memiliki waktu O(n log n). Dengan asumsi bahwa pivot dipilih secara acak atau semi-ideal, array akan dibagi menjadi dua subarray yang cukup seimbang di setiap iterasi rekursi. Ini membuat algoritma sangat cepat untuk data acak. Meskipun tidak selalu menghasilkan pembagian yang sempurna, performa rata-rata tetap efisien karena pembagian mendekati ideal.")
