import subprocess
def menu():
    while True:
        print("\nSelamat datang ke dalam Quizz")
        print("Pilihlah Quizz yang akan anda kerjakan:")
        print("1. Quiz IPA")
        print("2. Quiz Matematika")
        print("3. Quiz Agama")
        print("4. Quiz Bahasa")
        print("5. Keluar")  # Added an option to exit the menu

        pilihan = input("Masukkan nomor pilihan Anda (1, 2, 3, 4, atau 5): ")

        if pilihan == "1":
            ipa()
        elif pilihan == "2":
            matematika()
        elif pilihan == "3":
            agama()
        elif pilihan == "4":
            bahasa()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, kembali ke menu utama.")

def ipa():
    print("Ini adalah Quiz IPA. (Tambahkan pertanyaan di sini)")



def matematika():
    print("Ini adalah Quiz Matematika. (Tambahkan pertanyaan di sini)")



def agama():
    print("Ini adalah Quiz Agama. (Tambahkan pertanyaan di sini)")



def bahasa():
    print("Ini adalah Quiz Bahasa. (Tambahkan pertanyaan di sini)")
    


def menu_quiz():
    print("\n--- batas waktu ---")
    # Menjalankan script 'potional_quizz.py' sebagai skrip eksternal
    subprocess.run(["python3", "batas_waktu.py"])  # Gunakan 'python3' jika menggunakan Python 3

# Memanggil fungsi menu
menu()
