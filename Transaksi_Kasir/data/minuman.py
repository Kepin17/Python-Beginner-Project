def drinks():
    
    es_teh = 7000
    es_susu_kambing = 7500
    es_susu_milo = 8000
    es_coffe_latte = 12000

    print("Menu minuman")
    print("1.Es Teh             = Rp. 7,000,00")
    print("2.Es Susu Kambing    = Rp. 7,500,00")
    print("3.Es Susu Milo       = Rp. 8,000,00")
    print("4.Es Cofee Latte     = Rp. 12,000,00")
    order = int(input("Pilihan kamu : "))
    if order ==1:
        jumlah = int(input("Kamu mau pesan berapa? : "))
        hasil = es_teh * jumlah
        print(f"Kamu memesan es teh dengan harga Rp. {hasil:,}")
   
    elif order ==2:
        jumlah = int(input("Kamu mau pesan berapa? : "))
        hasil = es_susu_kambing * jumlah
        print(f"Kamu memesan es susu kambing dengan harga Rp. {hasil:,}")
   
    elif order ==3:
        jumlah = int(input("Kamu mau pesan berapa? : "))
        hasil = es_susu_milo * jumlah
        print(f"Kamu memesan es susu milo dengan harga Rp. {hasil:,}")
      
    elif order ==4:
        jumlah = int(input("Kamu mau pesan berapa? : "))
        hasil = es_coffe_latte * jumlah
        print(f"Kamu memesan es coffee latte dengan harga Rp. {hasil:,}")
      
    else:
        print("\nMenu belum tersedia")




