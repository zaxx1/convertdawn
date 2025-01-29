import json
import time

# Menambahkan delay 10 detik sebelum mulai memproses
print("Menunggu 10 detik sebelum mulai...")
time.sleep(10)

# Membaca data dari file data.txt
with open('data.txt', 'r') as file_in:
    lines = file_in.readlines()

# Menyiapkan list untuk menyimpan data yang telah diformat
formatted_data = []

# Memproses setiap baris dalam file
for line in lines:
    # Menghapus karakter newline dan membagi berdasarkan tanda ':'
    parts = line.strip().split(":")
    if len(parts) == 2:
        # Membuat dictionary dengan format yang diinginkan
        formatted_data.append({
            "Email": parts[0],
            "Token": parts[1]
        })

# Menyimpan hasil dalam format JSON ke file account.json
with open('account.json', 'w') as file_out:
    json.dump(formatted_data, file_out, indent=4)

print("Data telah diubah dan disimpan dalam file account.json.")
