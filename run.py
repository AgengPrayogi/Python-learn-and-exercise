"""
TUTORIAL INTERAKTIF: Big O Notation & Struktur Data Python
Jalankan kode ini section by section untuk memahami cara kerjanya!
"""

import time
import random

print("=" * 60)
print("BAGIAN 1: MEMAHAMI BIG O NOTATION DENGAN PENGUKURAN WAKTU")
print("=" * 60)

# Function untuk mengukur waktu eksekusi
def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, (end - start) * 1000  # dalam milliseconds

# O(1) - Constant Time
def constant_time(arr):
    """Selalu 1 operasi, tidak peduli ukuran array"""
    return arr[0] if arr else None

# O(n) - Linear Time
def linear_time(arr, target):
    """Operasi sebanyak n elemen"""
    for item in arr:
        if item == target:
            return True
    return False

# O(n²) - Quadratic Time
def quadratic_time(arr):
    """Nested loop - n x n operasi"""
    pairs = []
    for i in arr:
        for j in arr:
            pairs.append((i, j))
    return pairs

# Test dengan ukuran data berbeda
print("\n🔍 Eksperimen 1: Perbandingan Kompleksitas Waktu\n")

sizes = [100, 1000, 5000]
for size in sizes:
    data = list(range(size))
    
    # Test O(1)
    _, time1 = measure_time(constant_time, data)
    
    # Test O(n)
    _, time2 = measure_time(linear_time, data, size - 1)  # cari elemen terakhir
    
    print(f"Ukuran data: {size:,}")
    print(f"  O(1) - Constant  : {time1:.4f} ms (selalu cepat!)")
    print(f"  O(n) - Linear    : {time2:.4f} ms")
    print()

print("💡 Perhatikan: O(1) selalu cepat, O(n) makin lambat seiring data bertambah\n")

print("=" * 60)
print("BAGIAN 2: LIST - Struktur Data Berurutan")
print("=" * 60)

# Membuat list
fruits = ["apple", "banana", "cherry", "durian"]
print(f"\n📋 List awal: {fruits}")

# Operasi dasar LIST
print("\n🔧 Operasi List:")

# 1. Akses by index - O(1)
print(f"1. Akses index [1]: {fruits[1]} - O(1) ✅ Cepat!")

# 2. Append di akhir - O(1)
fruits.append("elderberry")
print(f"2. Append 'elderberry': {fruits} - O(1) ✅ Cepat!")

# 3. Insert di tengah - O(n)
fruits.insert(2, "coconut")
print(f"3. Insert 'coconut' di index 2: {fruits} - O(n) ⚠️ Lambat!")
print("   (Semua elemen setelahnya harus digeser)")

# 4. Search nilai - O(n)
start = time.perf_counter()
found = "cherry" in fruits
end = time.perf_counter()
print(f"4. Cari 'cherry': {found} - O(n) ⚠️ Harus loop!")

# 5. Remove - O(n)
fruits.remove("banana")
print(f"5. Remove 'banana': {fruits} - O(n) ⚠️ Lambat!")

# 6. Slicing - O(k) dimana k = jumlah elemen yang di-slice
print(f"6. Slice [1:4]: {fruits[1:4]} - O(k)")

# List comprehension - powerful!
print("\n🚀 List Comprehension:")
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(f"Original: {numbers}")
print(f"Squared: {squared}")

even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even only: {even_numbers}")

print("\n=" * 60)
print("BAGIAN 3: DICTIONARY - Key-Value Mapping")
print("=" * 60)

# Membuat dictionary
student_scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 88
}
print(f"\n📚 Dictionary awal:\n{student_scores}")

print("\n🔧 Operasi Dictionary:")

# 1. Lookup by key - O(1) ⭐ SUPER CEPAT!
print(f"1. Cari score 'Bob': {student_scores['Bob']} - O(1) ⚡ INSTANT!")

# 2. Add/Update - O(1)
student_scores["Eve"] = 94
print(f"2. Tambah 'Eve': {student_scores} - O(1) ⚡")

# 3. Delete - O(1)
del student_scores["Charlie"]
print(f"3. Hapus 'Charlie': {student_scores} - O(1) ⚡")

# 4. Check key existence - O(1)
print(f"4. Apakah 'Alice' ada? {'Alice' in student_scores} - O(1) ⚡")

# Use case: Counting frequency
print("\n📊 Use Case: Menghitung Frekuensi Kata")
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(f"Words: {words}")
print(f"Frequency: {frequency}")

# Dictionary methods
print("\n🔑 Dictionary Methods:")
print(f"Keys: {list(student_scores.keys())}")
print(f"Values: {list(student_scores.values())}")
print(f"Items: {list(student_scores.items())}")

print("\n=" * 60)
print("BAGIAN 4: SET - Koleksi Unik Tanpa Duplikat")
print("=" * 60)

# Membuat set
colors = {"red", "green", "blue", "red", "yellow"}  # duplikat otomatis dihapus
print(f"\n🎨 Set (duplikat hilang): {colors}")

print("\n🔧 Operasi Set:")

# 1. Add - O(1)
colors.add("purple")
print(f"1. Add 'purple': {colors} - O(1) ⚡")

# 2. Remove - O(1)
colors.remove("green")
print(f"2. Remove 'green': {colors} - O(1) ⚡")

# 3. Membership check - O(1) ⭐ SUPER CEPAT!
print(f"3. Apakah 'blue' ada? {'blue' in colors} - O(1) ⚡ INSTANT!")

# Set operations
print("\n🧮 Operasi Matematika Set:")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A | B): {set_a | set_b} - Gabungan semua")
print(f"Intersection (A & B): {set_a & set_b} - Yang sama")
print(f"Difference (A - B): {set_a - set_b} - Yang ada di A saja")
print(f"Symmetric Diff (A ^ B): {set_a ^ set_b} - Yang tidak sama")

# Use case: Remove duplicates
print("\n🔄 Use Case: Menghapus Duplikat")
numbers_with_dup = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique_numbers = list(set(numbers_with_dup))
print(f"Original: {numbers_with_dup}")
print(f"Unique: {unique_numbers}")

print("\n=" * 60)
print("BAGIAN 5: PERBANDINGAN PERFORMA - LIST vs SET")
print("=" * 60)

# Membuat data besar
large_list = list(range(100000))
large_set = set(range(100000))
target = 99999  # elemen terakhir

print(f"\n⏱️  Mencari angka {target} dalam 100,000 elemen:\n")

# Search di LIST - O(n)
start = time.perf_counter()
result = target in large_list
end = time.perf_counter()
list_time = (end - start) * 1000
print(f"LIST  - O(n)  : {list_time:.4f} ms ⚠️ Lambat!")

# Search di SET - O(1)
start = time.perf_counter()
result = target in large_set
end = time.perf_counter()
set_time = (end - start) * 1000
print(f"SET   - O(1)  : {set_time:.4f} ms ⚡ SUPER CEPAT!")

print(f"\n💡 SET lebih cepat {list_time/set_time:.0f}x dari LIST untuk searching!")

print("\n" + "=" * 60)
print("BAGIAN 6: REAL WORLD EXAMPLE")
print("=" * 60)

print("\n🌐 Contoh: Sistem Validasi Username\n")

# Bad approach: menggunakan list
registered_users_list = [f"user{i}" for i in range(10000)]

# Good approach: menggunakan set
registered_users_set = set(registered_users_list)

username_to_check = "user9999"

# Cek dengan list - lambat
start = time.perf_counter()
available_list = username_to_check not in registered_users_list
end = time.perf_counter()
time_list = (end - start) * 1000

# Cek dengan set - cepat
start = time.perf_counter()
available_set = username_to_check not in registered_users_set
end = time.perf_counter()
time_set = (end - start) * 1000

print(f"Cek ketersediaan username '{username_to_check}':")
print(f"  Menggunakan LIST: {time_list:.4f} ms ⚠️")
print(f"  Menggunakan SET : {time_set:.4f} ms ⚡")
print(f"  SET {time_list/time_set:.0f}x lebih cepat!\n")

print("=" * 60)
print("📝 RANGKUMAN")
print("=" * 60)
print("""
┌─────────────┬──────────┬──────────┬─────────┬──────────────┐
│ Struktur    │ Akses    │ Search   │ Insert  │ Kapan Pakai  │
├─────────────┼──────────┼──────────┼─────────┼──────────────┤
│ LIST        │ O(1)     │ O(n)     │ O(n)    │ Butuh urutan │
│ DICT        │ O(1)     │ O(1)     │ O(1)    │ Key-value    │
│ SET         │ N/A      │ O(1)     │ O(1)    │ Unik + cepat │
└─────────────┴──────────┴──────────┴─────────┴──────────────┘

✅ Gunakan LIST: Butuh urutan, akses by index, boleh duplikat
✅ Gunakan DICT: Lookup cepat by key, mapping data
✅ Gunakan SET: Tidak boleh duplikat, cek membership cepat

Prinsip: Pilih struktur data berdasarkan operasi yang PALING SERING!
""")