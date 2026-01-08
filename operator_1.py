# Operator Arithmetic
a = 5 +3 
print(a) # 8 namanya addition
b = 5 - 3
print(b) # 2 namanya subtraction
c = 5 * 3
print(c) # 15 namanya multiplication
d = 5 / 3
print(d) # 1.6666666666666667 namanya division (Membagi 5 dengan 3, hasil berupa float)
e = 5 % 3
print(e) # 2 namanya modulus (Menghasilkan sisa pembagian 5 dengan 3)
f = 5 ** 3
print(f) # 125 namanya exponentiation (Menghitung 5 pangkat 3)
g = 5 // 3
print(g) # 1 namanya floor division (Membagi 5 dengan 3, hasil dibulatkan ke bawah)
h = 5 + 3 * 2 - 1 / 2 ** 3 // 4 % 5
print(h) # 8.875 namanya operator precedence (Operator di sini mengikuti operator precedence (prioritas operasi). Operasi dieksekusi dengan prioritas lebih tinggi (pangkat, perkalian, pembagian, modulus, floor division) terlebih dahulu sebelum penjumlahan dan pengurangan.)
# Operator Assignment
a = 5
print(a) # 5
a += 3
print(a) # 8 namanya addition assignment (Menambahkan 3 ke nilai a yang sudah ada (5) sehingga menjadi 8.)
a -= 3
print(a) # 5 namanya subtraction assignment (Mengurangi 3 dari nilai a.)
a *= 3
print(a) # 15 namanya multiplication assignment (Mengalikan nilai a dengan 3.)
a /= 3
print(a) # 5.0 namanya division assignment (Membagi nilai a dengan 3.)
a %= 3
print(a) # 2.0 namanya modulus assignment (Menghitung sisa pembagian nilai a dengan 3.)
a **= 3
print(a) # 8.0 namanya exponentiation assignment (Menghitung nilai a pangkat 3.)
a //= 3
print(a) # 2.0 namanya floor division assignment (Membagi nilai a dengan 3 dan membulatkan hasilnya ke bawah.)
# Operator Comparison
x = 5 > 3  # Output: True (lebih besar dari)
print(x)
y = 5 < 3  # Output: False (kurang dari)
print(y)
z = 5 == 3  # Output: False (sama dengan)
print(z)
a = 5 != 3  # Output: True (tidak sama dengan)
print(a)
# Operator Logical
result = (5 > 3) and (10 < 20)   # Output: False (dan) (Kedua kondisi harus True agar hasilnya True.)
("Catatan: Komentar di kode asli tertulis Output: False, namun seharusnya hasilnya True karena kedua kondisi benar")
print(result)
result = (5 > 3) or (10 > 20)    # Output: True (atau) (Jika salah satu kondisi benar, hasilnya True)
print(result)
result = not (5 > 3)             # Output: False (tidak) (Membalikkan nilai boolean. Karena (5 > 3) adalah True, maka not mengubahnya menjadi False.)
print(result)