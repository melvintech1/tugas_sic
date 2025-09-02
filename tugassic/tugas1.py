def konversi_suhu(nilai, dari, ke):
    """
    Fungsi untuk mengkonversi suhu dari satu satuan ke satuan lainnya
    
    Parameters:
    nilai (float): nilai suhu yang akan dikonversi
    dari (str): satuan asal ("c", "f", "k")
    ke (str): satuan tujuan ("c", "f", "k")
    
    Returns:
    float: hasil konversi suhu
    str: pesan error jika input tidak valid
    """
    
    # Konversi ke lowercase untuk case insensitive
    dari = dari.lower()
    ke = ke.lower()
    
    # Validasi satuan
    satuan_valid = ["c", "f", "k"]
    if dari not in satuan_valid or ke not in satuan_valid:
        return "Error: Satuan harus 'c', 'f', atau 'k'"
    
    # Validasi nilai untuk Kelvin
    if dari == "k" and nilai < 0:
        return "Error: Kelvin tidak boleh negatif"
    
    try:
        nilai = float(nilai)
    except (ValueError, TypeError):
        return "Error: Nilai suhu harus berupa angka"
    
    # Konversi ke Celsius terlebih dahulu
    if dari == "c":
        celsius = nilai
    elif dari == "f":
        celsius = (nilai - 32) * 5/9
    elif dari == "k":
        celsius = nilai - 273.15
    
    # Konversi dari Celsius ke satuan tujuan
    if ke == "c":
        hasil = celsius
    elif ke == "f":
        hasil = (celsius * 9/5) + 32
    elif ke == "k":
        hasil = celsius + 273.15
        # Validasi kembali untuk Kelvin setelah konversi
        if hasil < 0:
            return "Error: Hasil konversi ke Kelvin tidak valid (negatif)"
    
    return round(hasil, 2)