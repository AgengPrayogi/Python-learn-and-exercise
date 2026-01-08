# Problem: Cek apakah ada nilai yang duplikat
def has_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
# Big O: O(n²) - LAMBAT!

# TUGAS: Buat versi cepat dengan Big O: O(n)
def has_duplicate_fast(arr):
    # Tulis kode kamu di sini
    
    # Hint: Gunakan set!
    test = set()
    for value in arr:
        if value in test:
            return True
        test.add(value)
    return False

# Test
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(has_duplicate_slow(test_data))  # True
print(has_duplicate_fast(test_data))  # harus True juga, tapi lebih cepat!