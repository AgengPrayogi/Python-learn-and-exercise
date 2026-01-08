# Struktur Dasar
"""
def nama_fungsi(parameter):
    # blok kode fungsi
    return hasil
"""
# contoh fungsi sederhana
def greet(name):
    """
    Fungsi ini menyapa pengguna dengan nama yang diberikan.
    :param name: Nama pengguna
    :return: Pesan sapaan
    """
    return f"Hello, {name}!"
massage = greet("Alice")
print(massage)  # Output: Hello, Alice
# Parameter, Argumen, dan Nilai Kembalian (Parameters, Arguments, and Return Values)
def add(a, b=5):
    """
    Fungsi ini menjumlahkan dua angka.
    :param a: Angka pertama
    :param b: Angka kedua
    :return: Hasil penjumlahan
    """
    return a + b
result = add(10)
print(result)  # Output: 15
# Lambda Functions untuk Operasi Anonim (Lambda Functions for Anonymous Operations)
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Fungsi Rekursif (Recursive Functions)
def factorial(n):
    """
    Fungsi ini menghitung faktorial dari n.
    :param n: Angka untuk menghitung faktorial
    :return: Faktorial dari n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(result)  # Output: 120
# Fungsi dengan Parameter Posisi dan Kata Kunci (Positional and Keyword Arguments)
def describe_pet(pet_name, animal_type='dog'):
    """
    Fungsi ini mendeskripsikan hewan peliharaan.
    :param pet_name: Nama hewan peliharaan
    :param animal_type: Jenis hewan peliharaan
    """
    print(f"I have a {animal_type} named {pet_name}.")
describe_pet('Buddy')  # Output: I have a dog named Buddy.
describe_pet('Whiskers', 'cat')  # Output: I have a cat named Whiskers.
# Fungsi dengan Parameter Variabel (Variable-Length Arguments)
def make_pizza(size, *toppings):
    """
    Fungsi ini membuat pizza dengan ukuran dan topping yang diberikan.
    :param size: Ukuran pizza
    :param toppings: Topping pizza
    """
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(12, 'pepperoni', 'mushrooms', 'green peppers')
# Fungsi dengan Parameter Kata Kunci Variabel (Keyword-Only Arguments)
def build_profile(first, last, **user_info):
    """
    Fungsi ini membangun profil pengguna dengan informasi yang diberikan.
    :param first: Nama depan
    :param last: Nama belakang
    :param user_info: Informasi tambahan tentang pengguna
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('John', 'Doe', location='New York', age=30)
print(user_profile)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'location': 'New York', 'age': 30}
# Fungsi Bawaan (Built-in Functions)
"""
Fungsi Bawaan yang Umum:

len(): Mengembalikan panjang objek.
print(): Mencetak teks ke konsol.
type(): Menentukan tipe objek.
sum(): Menghitung total dari urutan angka.
"""
# Fungsi bawaan Python yang sering digunakan
print(len("Hello"))  # Output: 5 (Menghitung panjang string)
print(max([1, 2, 3]))  # Output: 3 (Mengambil nilai maksimum dari list)
print(min([1, 2, 3]))  # Output: 1 (Mengambil nilai minimum dari list)
print(sum([1, 2, 3]))  # Output: 6 (Menjumlahkan semua elemen dalam list)
angka = 1, 2, 3, 4
print(type(angka))  # Output: <class 'tuple'> (Menentukan tipe data dari variabel angka)

# Argumen Default
def sapa(nama="Tamu"):
    return f"Halo, {nama}!"

print(sapa())          # Output: Halo, Tamu!
print(sapa("Alice"))   # Output: Halo, Alice!
# Argumen Panjang Variabel
def jumlah_semua(*args):
    return sum(args)

print(jumlah_semua(1, 2, 3))         # Output: 6
print(jumlah_semua(10, 20, 30, 40))  # Output: 100