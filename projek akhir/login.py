import subprocess

# Dictionary untuk menyimpan username dan password
user_data = {
    "1": "12",
    "user2": "mypassword",
    "user3": "securepass"
}

def menu():
    while True:
        print("\nSelamat datang! Silakan pilih opsi:")
        print("1. Login")
        print("2. Tambah Pengguna Baru")
        print("3. Keluar")

        pilihan = input("Masukkan nomor pilihan Anda (1, 2, 3, ): ")

        if pilihan == "1":
            if login():
                menu_opsional()
        elif pilihan == "2":
            tambah_pengguna()
        elif pilihan == "3":
            print("Keluar dari sistem. Sampai jumpa!")
        elif pilihan == "4":
            menu_quiz()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if username in user_data and user_data[username] == password:
        print(f"Login berhasil! Selamat datang, {username}")
        return True  # Login berhasil
    else:
        print("Username atau password salah. Silakan coba lagi.")
        return False  # Login gagal

def tambah_pengguna():
    print("\n--- Tambah Pengguna Baru ---")
    username = input("Masukkan username baru: ")

    if username in user_data:
        print("Username sudah ada. Silakan coba dengan username lain.")
    else:
        password = input("Masukkan password: ")
        user_data[username] = password
        print(f"Pengguna {username} berhasil ditambahkan!")

def menu_opsional():
    while True:
        print("\n--- Menu Opsional ---")
        print("1. Lihat Profil")
        print("2. Pengaturan Akun")
        print("3. Kembali ke Menu Utama")
        print("4. Masuk Ke Menu Quizz")
        pilihan = input("Masukkan nomor pilihan Anda (1, 2, 3, atau 4): ")

        if pilihan == "1":
            print("Menampilkan profil pengguna...")
        elif pilihan == "2":
            print("Mengakses pengaturan akun...")
        elif pilihan == "3":
            print("Kembali ke menu utama...")
            break
        elif pilihan == "4":
            menu_quiz()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_quiz():
    print("\n--- Masuk ke Menu Quizz ---")
    # Menjalankan script 'potional_quizz.py' sebagai skrip eksternal
    subprocess.run(["python3", "optional_quizz.py"])  # Gunakan 'python3' jika menggunakan Python 3

# Fungsi utama untuk menjalankan script
if __name__ == "__main__":
    menu()
