import random


def price():

      ticket_prices = random.randint(10 , 40)
      ticket_price = ticket_prices
      buy_ticket = int(input("\nKamu mau pesan berapa tiket : "))
      print("\nKamu mau duduk di mana?")
      print("")
      print("==============================Layar===============================")
      print()
      print()
      print("A1 A2 A3  A4 A5 A6  A7 A8 A9       B1 B2 B3  B4 B5 B6 B7 B8 B9    ")
      print("C1 C2 C3  C4 C5 C6  C7 C8 C9       D1 D2 D3  D4 D5 D6 D7 D8 D9    ")
      print("E1 E2 E3  E4 E5 E6  E7 E8 E9       F1 F2 F3  F4 F5 F6 F7 F8 F9    ")
      print("G1 G2 G3  G4 G5 G6  G7 G8 G9       H1 H2 H3  H4 H5 H6 H7 H8 H9    ")
      print("I1 I2 I3  I4 I5 I6  I7 I8 I9       J1 J2 J3  J4 J5 J6 J7 J8 J9    ")
      print("K1 K2 K3  K4 K5 K6  K7 K8 K9       L1 L2 L3  L4 L5 L6 L7 L8 L9    ")
      print("M1 M2 M3  M4 M5 M6  M7 M8 M9       N1 N2 N3  N4 N5 N6 N7 N8 N9    ")
      print("O1 O2 O3  O4 O5 O6  O7 O8 O9       P1 P2 P3  P4 P5 P6 P7 P8 P9    ")
      print("===========================Proyektor============================  ")


      user_choise = str(input("Your  Choose : "))

      if buy_ticket >= 5:
          tiket = buy_ticket * ticket_price
          ppn = tiket * 10/100
          disc = tiket * 5/100
          total = int((tiket + ppn) - disc) 

          print()
          print("=====================================")
          print("  Kamu mendapatkan diskon sebesar 5% ")
          print("=====================================")
          print(f"\n Total tiket : {buy_ticket} orang ")
          print(f" Total biaya   : ${total}             ")
          print(f" Nomor Kursi   : {user_choise}      ")
          print("=====================================")
          print("silahkan melakukan pembayaran")
      else:
          tiket = buy_ticket * ticket_price
          ppn = tiket * 10/100
          total = int((tiket + ppn)) 
          print()
          print("=====================================")
          print("           Harga tiket               ")
          print("=====================================")
          print(f" Total tiket   : {buy_ticket} orang ")
          print(f" Total biaya   : ${total}           ")
          print(f" Nomor Kursi   : {user_choise}      ")
          print("=====================================")
          print("silahkan melakukan pembayaran")


  

      
     
