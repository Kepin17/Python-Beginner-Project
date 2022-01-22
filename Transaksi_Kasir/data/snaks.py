def snaks():
    
    PisangGoreng = 7000
    SingkongGoreng = 7500
    Gorengan = 8000
    TempeTahu = 12000

    print("Menu minuman")
    print("1.Pisang goreng      = Rp. 7,000,00")
    print("2.Singkong goreng    = Rp. 7,500,00")
    print("3.Gorengan           = Rp. 8,000,00")
    print("4.Tempe dan Tahu     = Rp. 12,000,00")
    order = int(input("Pilihan kamu : "))
    if order ==1:
        jumlah = int(input("Kamu mau pesan berapa? : "))
        hasil = PisangGoreng * jumlah
        print(f"Kamu memesan pisang goreng dengan harga Rp. {hasil:,}")
   
    elif order ==2:
        jumlah = int(input("Kamu mau pesan berapa? : "))
        hasil = SingkongGoreng * jumlah
        print(f"Kamu memesan singkong goreng dengan harga Rp. {hasil:,}")
   
    elif order ==3:
        jumlah = int(input("Kamu mau pesan berapa? : "))
        hasil = Gorengan * jumlah
        print(f"Kamu memesan gorengan dengan harga Rp. {hasil:,}")
      
    elif order ==4:
        hargaTempe = 6000
        hargaTahu = 6000
        jumlahTempe = int(input("Kamu mau pesan tempe berapa? : "))
        jumlahTahu = int(input("Kamu mau pesan tahu berapa? : "))
        total_order = (hargaTempe * jumlahTempe) + (hargaTahu * jumlahTahu)
        hasil = total_order
        print(f"Kamu memesan Tempe dan Tahu dengan harga Rp. {hasil:,}")
      
    else:
        print("\nMenu belum tersedia")



