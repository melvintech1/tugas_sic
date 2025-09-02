from tugas1 import konversi_suhu

def main():
    print("=" * 50)
    print("PROGRAM KONVERSI SUHU RUANGAN")
    print("=" * 50)
    
    # Daftar satuan yang tersedia
    satuan = {
        "c": "Celsius",
        "f": "Fahrenheit", 
        "k": "Kelvin"
    }
    
    # Tampilkan pilihan satuan
    print("\nSatuan yang tersedia:")
    for kode, nama in satuan.items():
        print(f"{kode.upper()} - {nama}")
    
    # Input dari user
    print("\n" + "-" * 30)
    
    # Input satuan asal
    while True:
        dari = input("Masukkan satuan asal (c/f/k): ").strip().lower()
        if dari in satuan:
            break
        print("Error: Pilih 'c', 'f', atau 'k'!")
    
    # Input satuan tujuan  
    while True:
        ke = input("Masukkan satuan tujuan (c/f/k): ").strip().lower()
        if ke in satuan:
            break
        print("Error: Pilih 'c', 'f', atau 'k'!")
    
    # Input nilai suhu
    while True:
        try:
            nilai = float(input("Masukkan nilai suhu: "))
            
            # Validasi khusus untuk Kelvin
            if dari == "k" and nilai < 0:
                print("Error: Kelvin tidak boleh negatif!")
                continue
                
            break
        except ValueError:
            print("Error: Masukkan angka yang valid!")
    
    # Proses konversi
    print("\n" + "=" * 50)
    hasil = konversi_suhu(nilai, dari, ke)
    
    # Tampilkan hasil
    if isinstance(hasil, str):
        print(f"ERROR: {hasil}")
    else:
        print(f"HASIL KONVERSI:")
        print(f"{nilai}° {satuan[dari].upper()} = {hasil}° {satuan[ke].upper()}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()