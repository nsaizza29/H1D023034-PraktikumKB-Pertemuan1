import random
from datetime import datetime

# Daftar menu makanan dan minuman
menu_makanan = {
    1: ("Rice Bowl", 25000),
    2: ("Ayam", 28000),
    3: ("Chicken Katsu", 30000)
}

menu_minuman = {
    1: ("Mineral", 8000),
    2: ("Ice Tea", 10000),
    3: ("Ocha", 9000)
}

# Menampilkan menu
def tampilkan_menu(menu, kategori):
    print(f"\n=== Menu {kategori} ===")
    for nomor, (nama, harga) in menu.items():
        print(f"{nomor}. {nama} - Rp{harga:,}")

# Memproses pesanan
def pesan_menu(menu, kategori):
    pesanan = []
    while True:
        tampilkan_menu(menu, kategori)
        pilihan = input("Pilih nomor menu (0 untuk selesai): ")

        if pilihan == "0":
            break
        elif pilihan.isdigit() and int(pilihan) in menu:
            pesanan.append(menu[int(pilihan)])
            print(f"{menu[int(pilihan)][0]} ditambahkan ke pesanan.")
        else:
            print("Pilihan tidak tersedia, coba lagi.")
    return pesanan

# Fungsi 
def main():
    print("Selamat datang di Restoran KITA!")
    
    pesanan = pesan_menu(menu_makanan, "Makanan") + pesan_menu(menu_minuman, "Minuman")

    if pesanan:
        total = sum(harga for _, harga in pesanan)
        waktu_pesanan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        kode_pesanan = random.randint(1000, 9999)

        print("\n=== Struk Pemesanan ===")
        for nama, harga in pesanan:
            print(f"- {nama} - Rp{harga:,}")
        print(f"Total Bayar: Rp{total:,}")
        print(f"Waktu Pesanan: {waktu_pesanan}")
        print(f"Kode Pesanan: #{kode_pesanan}")
        print("Terima kasih telah memesan!")
    else:
        print("Anda tidak memesan apa pun.")


# Menjalankan program
if __name__ == "__main__":
    main()
