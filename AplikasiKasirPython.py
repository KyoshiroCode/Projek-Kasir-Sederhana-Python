TotalHarga = {
    "tahu": 1500,
    "tempe": 2500,
    "daging": 5000,
    "susu": 3000
}

def pembayaran():
    total_belanja = 0
    while True:
        print("\n======== Toko Makmur ========")
        for nama, harga in TotalHarga.items():
            print(f"- {nama.title()} : Rp{harga}")
        print("==============================")

        item = input("Mau beli apa: ").lower()
        if item not in TotalHarga:
            print("Barang tidak tersedia.")
            continue

        try:
            jumlah = int(input(f"Berapa {item} yang mau dibeli: "))
            subtotal = jumlah * TotalHarga[item]
            total_belanja += subtotal
            print(f"Subtotal: Rp{subtotal}")
        except:
            print("Jumlah tidak valid!")
            continue

        lagi = input("Mau beli lagi? (y/n): ").lower()
        if lagi != 'y':
            break

    print(f"\nTotal yang harus dibayar: Rp{total_belanja}")
    kembalian(total_belanja)

def kembalian(total):
    try:
        bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
    except:
        print("Input tidak valid.")
        return

    if bayar < total:
        print("Uang anda kurang!")
        return

    kembali = bayar - total
    print(f"Kembalian: Rp{kembali}")

    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    for p in pecahan:
        lembar = kembali // p
        if lembar:
            print(f"Pecahan uang Rp{p} sebanyak {lembar} lembar")
            kembali %= p

pembayaran()
