from data import food , tryAgain , drinks , snaks

def menu():

    print('======================================================================================')
    print("=                                     OmniFood                                       =")
    print('======================================================================================')
    print("= 1. Foods                                                                           =")
    print("= 2. Drinks                                                                          =")
    print("= 3. Snaks                                                                           =")
    print('======================================================================================')

    user = int(input("Pilihan kamu : "))
    if user ==1:
        food()

    elif user ==2:
        drinks()
  
    elif user ==3:
        snaks()
    else:
        print("\nPilihan kamu tidak tersedia :(\n")
        
menu()
while tryAgain():
    menu()

print("\nAkhir dari program , Terimakasih XD")
print("Project Name : Transaksi Kasir")
   

