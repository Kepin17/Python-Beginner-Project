# import random
from data import jadwal , price , tryAgain 
from data import Action , Romance , War , Family

def mainMenu():
      print("============================================================================")
      print("                          Welcome to Vin Studio                             ")
      print("============================================================================")
      user_name = str(input("please enter yout name : "))
      print(f"\nHi {user_name}!")
      print("Kamu mau memonton film bergenre apa?")
      print("\n1.Action")
      print("2.Romance")
      print("3.War")
      print("4.Family")
      user_choise = int(input("Your choise : "))

      if user_choise ==1:
            print(f"\nyeay {user_name}!")
            print("Kamu berhasil memilih genre Action , Yuk liat daftar filmnya!")
            Action()
            jadwal()
            price()
                        
            pay = input("\nMelanjutkan proses pembayaran? yes / no : ")
            pay = pay.upper()
            if pay =="YES":
                  print()
                  print("===============================")
                  print("Kamu mau membayar  via apa?    ")
                  print("1.M-Banking")
                  print("2.cash")
                  print("===============================")
                  user_choise = int(input("Your choose : "))
                  if user_choise ==1:
                              print("Pemayaran berhasil,silahkan tunjukan tiket kamu kepada petugas")
                  elif user_choise ==2:
                              print("Silahkan tunjukan info pembayaran ini kepada petugas,untuk melakukan pembayaran")

            else:             
                  while tryAgain():
                        mainMenu()
                  
            
      elif user_choise ==2:
            print(f"\nyeay {user_name}!")
            print("Kamu berhasil memilih genre Romance , Yuk liat daftar filmnya!")
            Romance()
            jadwal()
            price()
                        
            pay = input("\nMelanjutkan proses pembayaran? yes / no : ")
            pay = pay.upper()
            if pay =="YES":
                  print()
                  print("===============================")
                  print("Kamu mau membayar  via apa?    ")
                  print("1.M-Banking")
                  print("2.cash")
                  print("===============================")
                  user_choise = int(input("Your choose : "))
                  if user_choise ==1:
                              print("Pemayaran berhasil,silahkan tunjukan tiket kamu kepada petugas")
                  elif user_choise ==2:
                              print("Silahkan tunjukan info pembayaran ini kepada petugas,untuk melakukan pembayaran")

            else:             
                  while tryAgain():
                        mainMenu()
            
      elif user_choise ==3:
            print(f"\nyeay {user_name}!")
            print("Kamu berhasil memilih genre War , Yuk liat daftar filmnya!")
            War()
            jadwal()
            price()
                        
            pay = input("\nMelanjutkan proses pembayaran? yes / no : ")
            pay = pay.upper()
            if pay =="YES":
                  print()
                  print("===============================")
                  print("Kamu mau membayar  via apa?    ")
                  print("1.M-Banking")
                  print("2.cash")
                  print("===============================")
                  user_choise = int(input("Your choose : "))
                  if user_choise ==1:
                              print("Pemayaran berhasil,silahkan tunjukan tiket kamu kepada petugas")
                  elif user_choise ==2:
                              print("Silahkan tunjukan info pembayaran ini kepada petugas,untuk melakukan pembayaran")

            else:             
                  while tryAgain():
                        mainMenu()
            
      elif user_choise ==4:
            print(f"\nyeay {user_name}!")
            print("Kamu berhasil memilih genre Family , Yuk liat daftar filmnya!")
            Family()
            jadwal()
            price()
                        
            pay = input("\nMelanjutkan proses pembayaran? yes / no : ")
            pay = pay.upper()
            if pay =="YES":
                  print()
                  print("===============================")
                  print("Kamu mau membayar  via apa?    ")
                  print("1.M-Banking")
                  print("2.cash")
                  print("===============================")
                  user_choise = int(input("Your choose : "))
                  if user_choise ==1:
                              print("Pemayaran berhasil,silahkan tunjukan tiket kamu kepada petugas")
                              pilih = input("Mau pesan tiket lagi? yes or no : ")
                              pilih = pilih.upper()
                              if pilih =="YES":
                                          mainMenu()
                              else:
                                    print("Sampai Jumpa")            
                  elif user_choise ==2:
                              print("Silahkan tunjukan info pembayaran ini kepada petugas,untuk melakukan pembayaran")
                              pilih = input("Mau pesan tiket lagi? yes or no : ")
                              pilih = pilih.upper()
                              if pilih =="YES":
                                          mainMenu()
                              else:
                                    print("Sampai Jumpa")            

                              
            else:             
                  while tryAgain():
                        mainMenu()
            


mainMenu()

print("\nTerimakasih , Akhir dari program")
print("Nama Project : Pemesanan Bioskop")
print("by Kepin17")
