# Control Flow in Python
# Conditionals, Loops, and Exception Handling
age = 18
if age >= 18:
    print("You are an adult.") # Mengecek apakah nilai variabel age lebih besar atau sama dengan 18. Jika True, maka blok di bawahnya akan dijalankan
elif age == 18:
    print("You are exactly 18 years old.") # Penyempurnaan kondisi, akan mengecek apakah age sama dengan 18 jika kondisi sebelumnya tidak terpenuhi.(Perlu dicatat bahwa jika kondisi pertama terpenuhi, blok ini tidak akan dieksekusi meskipun nilainya 18.)
else:
    print("You are a minor.") # Untuk semua kondisi selain di atas (misalnya usia kurang dari 18), blok ini dijalankan.
# Looping through a list
# For loop Mengiterasi setiap elemen dalam list fruits dan mencetak setiap nilai
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# While loop
count = 0
while count < 5:
    print(count)
    count += 1
    # Selama kondisi count < 5 terpenuhi, loop akan terus berjalan.
    # Di setiap iterasi, nilai count dicetak kemudian ditambah 1 untuk mencegah loop tanpa akhir.

# Control loop with break and continue also pass
# for loop with break
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    """
    Mengiterasi nilai dari 0 sampai 9.
    Jika nilai i mencapai 5, perintah break akan menghentikan loop secara langsung.
    Hanya nilai sebelum 5 yang dicetak.
    """
# for loop with continue
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
    """
    Mengiterasi nilai dari 0 sampai 9.
    Jika i merupakan bilangan genap (i % 2 == 0), continue akan melewati sisa iterasi dan langsung ke iterasi berikutnya.
    Hanya nilai ganjil yang dicetak.
    """
# for loop with pass
for i in range(10):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    print(i)
    """
    pass adalah placeholder yang artinya “tidak melakukan apa-apa”.
    Dalam kondisi jika i adalah bilangan genap, perintah pass membuat program tidak melakukan tindakan khusus, lalu perintah di luar blok if tetap mencetak i.
    Berbeda dengan continue yang langsung melompat ke iterasi berikutnya, sehingga pada contoh ini tetap mencetak semua nilai dari 0 sampai 9.
    """
# Exception Handling
# Menggunakan try-except untuk menangani error
    try:
        # Meminta input dari pengguna dan mengkonversinya ke integer
        x = int(input("Enter a number: "))
        # Melakukan pembagian 10 dengan nilai input
        result = 10 / x
        print("Result:", result)
    except ZeroDivisionError:
    # Menangani error pembagian dengan nol
        print("Error: Cannot divide by zero.")
    except ValueError:
        # Menangani error jika input bukan angka yang valid
        print("Error: Invalid input. Please enter a valid number.")
    finally:
        # Blok ini akan selalu dieksekusi
        print("Process complete.")