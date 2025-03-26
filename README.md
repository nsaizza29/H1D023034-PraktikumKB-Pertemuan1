# PENJELASAN CODE!!!

# Import Library
- Random digunakan untuk membuat kode pesanan acak
- Datetime digunakan untuk mencatat waktu pemesanan				

# Daftar Menu
- menu_makanan dan menu_minuman adalah dictionary yang menyimpan daftar makanan & minuman beserta harga. Setiap item punya nomor menu, nama, dan harga

# Fungsi tampilkan_menu()
- Menampilkan daftar menu dengan nomor dan harga
- menu: dictionary yang berisi daftar makanan atau minuman
- kategori: jenis menu yang akan ditampilkan (Makanan/Minuman)
- Fungsi akan mencetak menu beserta harganya

# Fungsi pesan_menu()
- Memilih makanan/minuman berdasarkan nomor
- Looping while True berjalan terus sampai pengguna memilih 0 (selesai memesan)
- Jika input adalah angka yang sesuai dengan menu, item tersebut ditambahkan ke daftar pesanan
- Jika input "0", pemesanan selesai
- Jika input salah, muncul pesan error
- Hasil akhirnya adalah daftar pesanan pelanggan

# Fungsi main()
- Fungsi utama yang menjalankan seluruh program
- Menampilkan selamat datang kepada pengguna
- Memanggil pesan_menu() untuk: Memproses pemesanan makanan & minuman hasilnya disimpan di variabel pesanan
- Cek apakah ada pesanan jika ada, maka:
	Menghitung total harga dengan sum(harga for _, harga in pesanan)
	Mendapatkan waktu saat ini dengan datetime.now().strftime()
	Membuat kode pesanan acak dengan random.randint(1000, 9999)
	Menampilkan struk pemesanan
- Jika tidak ada pesanan, tampilkan pesan "Anda tidak memesan apa pun"

# Menjalankan Program
- Jika dijalankan langsung (__name__ == "__main__"), maka fungsi main() akan dieksekusi.
  
