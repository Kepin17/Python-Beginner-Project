def food():
    
            Nasi_Goreng_Pedas = 15000
            Nasi_Goreng_Seefood = 17000
            Nasi_Goreng_Special = 18000
            Nasi_Goreng_Teri = 17500
            mie_goreng_Seefood = 15000
            mie_goreng_Pedas   = 15500
            mie_goreng_special = 16000
            mie_goreng_Teri    = 17500
            print("\nMenu Makanan : \n")
            user_order = int(input("1.Nasi Goreng\n2.Mie Goreng\nPromo beli 2 diskon 25%\nPilih Menu : "))              
            if user_order ==1:
                print("\nKamu mau memesan nasi goreng apa?\n")
                print("1.Nasi goreng Seefood = Rp. 17,000,00\n2.Nasi goreng Pedas = Rp. 15,000,00")
                print("3.Nasi goreng special = Rp. 18,000")
                print("4.Nasi goreng Teri    = Rp. 17,500")

                order = int(input("Pilihan kamu :")) 
                if order ==1:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = Nasi_Goreng_Seefood * jumlah 
                          hargaKotor = (Nasi_Goreng_Seefood * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga nasi goreng seefood Rp. {hargabersih:,}"
                          print(hasil)

                      else :
                          harga = Nasi_Goreng_Seefood * jumlah
                          hasil = f"harga nasi goreng seefood Rp. {harga:,}"
                          print(hasil)

                        
                elif order ==2:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = Nasi_Goreng_Pedas * jumlah 
                          hargaKotor = (Nasi_Goreng_Pedas * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga nasi goreng seefood Rp. {hargabersih:,}"
                          print(hasil)

                      else :
                          harga = Nasi_Goreng_Pedas * jumlah
                          hasil = f"harga nasi goreng Pedas Rp. {harga:,}"
                          print(hasil)
                      
                elif order ==3:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = Nasi_Goreng_Special * jumlah 
                          hargaKotor = (Nasi_Goreng_Special * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga nasi goreng special Rp. {hargabersih:,}"
                          print(hasil)


                      else :
                          harga = Nasi_Goreng_Special * jumlah
                          hasil = f"harga nasi goreng Special Rp. {harga:,}"
                          print(hasil)
                      
            
                elif order ==4:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = jumlah * Nasi_Goreng_Teri 
                          hargaKotor = (Nasi_Goreng_Teri * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga nasi goreng Teri Rp. {hargabersih:,}"
                          print(hasil)


                      else :
                          harga = Nasi_Goreng_Teri * jumlah
                          hasil = f"harga nasi goreng Teri Rp. {harga:,}"
                          print(hasil)
                else:
                        print("maaf maenu belum terdaftar")      
            elif user_order == 2:
                print("\nKamu mau memesan nasi goreng apa?\n")
                print("1.mie goreng Seefood = Rp. 15,000,00")
                print("2.mie goreng Pedas   = Rp. 15,500,00")
                print("3.mie goreng special = Rp. 16,000")
                print("4.mie goreng Teri    = Rp. 17,500")

                order = int(input("Pilihan kamu :")) 
                if order ==1:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = mie_goreng_Seefood * jumlah 
                          hargaKotor = (mie_goreng_Seefood * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga mie goreng seefood Rp. {hargabersih:,}"
                          print(hasil)


                      else :
                          harga = mie_goreng_Seefood * jumlah
                          hasil = f"harga mie goreng seefood Rp. {harga:,}"
                          print(hasil)

                        
                elif order ==2:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = mie_goreng_Pedas * jumlah 
                          hargaKotor = (mie_goreng_Pedas * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga mie goreng pedas Rp. {hargabersih:,}"
                          print(hasil)


                      else :
                          harga = mie_goreng_Pedas * jumlah
                          hasil = f"harga mie goreng Pedas Rp. {harga:,}"
                          print(hasil)
                      
                elif order ==3:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = mie_goreng_special * jumlah 
                          hargaKotor = (mie_goreng_special * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga mie goreng special Rp. {hargabersih:,}"
                          print(hasil)


                      else :
                          harga = mie_goreng_special * jumlah
                          hasil = f"harga nasi goreng Special Rp. {harga:,}"
                          print(hasil)
                      
            
                elif order ==4:
                      jumlah = int(input("Kamu mau pesan berapa : "))
                      if jumlah ==2:
                          total = mie_goreng_Teri * jumlah 
                          hargaKotor = (mie_goreng_Teri * 2) * 25/100
                          hargabersih = total - hargaKotor
                          hasil = f"harga mie goreng teri Rp. {hargabersih:,}"
                          print(hasil)


                      else :
                          harga = mie_goreng_Teri * jumlah
                          hasil = f"harga mie goreng Teri Rp. {harga:,}"
                          print(hasil)
                else:
                        print("\nmaaf maenu belum terdaftar")      




                      
                              
