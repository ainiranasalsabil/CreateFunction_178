def konversisuhu(temperature, value):
    # Jika value adalah 'C', berarti kita ingin mengonversi dari Fahrenheit ke Celsius
    if value == 'C':
        # Rumus konversi dari Fahrenheit ke Celsius: (F - 32) * 5/9
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'  # Mengembalikan hasil konversi dan unit Celsius
    else:
        # Jika value bukan 'C', maka kita mengonversi dari Celsius ke Fahrenheit
        # Rumus konversi dari Celsius ke Fahrenheit: (C * 9/5) + 32
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'  # Mengembalikan hasil konversi dan unit Fahrenheit

# Contoh pertama: Mengonversi suhu dari Celsius ke Fahrenheit
celsius_temperature = 30  # Suhu dalam Celsius
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')  # Mengonversi ke Fahrenheit
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")  # Mencetak hasil

# Contoh kedua: Mengonversi suhu dari Fahrenheit ke Celsius
fahrenheit_temperature = 86  # Suhu dalam Fahrenheit
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')  # Mengonversi ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")  # Mencetak hasil





import math  # Library untuk operasi matematika, seperti penggunaan konstanta π (pi)

# Menggunakan fungsi lambda untuk menghitung luas lingkaran.
# Rumus luas lingkaran adalah π * r^2.
luas_lingkaran = lambda r: math.pi * r * r

jari_jari = 7  # Menetapkan nilai jari-jari lingkaran

# Memanggil fungsi lambda untuk menghitung luas lingkaran dengan jari-jari 7
area = luas_lingkaran(jari_jari)

# Menampilkan hasil dengan format 2 angka di belakang koma
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")

