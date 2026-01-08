# Problem: Cari dua angka yang jika dijumlahkan = target

def two_sum_slow(arr, target):
    """Solusi O(n²) - nested loop"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None

# TUGAS: Buat versi O(n) menggunakan dictionary!
def two_sum_fast(arr, target):
    # Hint: Simpan nilai yang sudah dilihat di dict
    # Key: angka, Value: index
    # definisikan dictionary kosong
    seen = {}
    # iterasi melalui array
    for index, number in enumerate(arr):
        # cari komplemen yang dibutuhkan
        complement = target - number
        # cek apakah komplemen sudah ada di dict
        if complement in seen:
            # jika ada, kembalikan indeks pasangan  
            return [seen[complement], index]
        # jika tidak ada, simpan angka dan indeksnya di dict
        seen[number] = index
    return None

# Test
nums = [2, 7, 11, 15]
target = 18
print(two_sum_slow(nums, target))  # [0, 1] karena nums[0] + nums[1] = 2 + 7 = 9
print(two_sum_fast(nums, target))  # harus sama, tapi lebih cepat!