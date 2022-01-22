


print("Games Suit\nSilahkan Pilih\n A Batu\n B Gunting\n C Kertas\n")

player1 = str(input("Masukan pilihanmu Player 1 : ")) 
player2 = str(input("Masukan Pilihanmu Player 2 : "))


# Batu
    
if player1=="A" and player2=="A" or player1=="Batu" and player2=="Batu":
    print("Battle Draw!\n")
    
elif player1=="A" and player2=="B" or player1=="Batu" and player2=="Gunting":
    print("Player 1 Win !\n")

elif player1=="A" and player2=="C" or player1=="Batu" and player2=="Kertas":
    print("Player 2 Win!\n")
    
# Gunting

elif player1=="B" and player2=="B" or player1=="Gunting" and player2=="Gunting":
    print("Battle Draw!\n")
    
elif player1=="B" and player2=="A" or player1=="Gunting" and player2=="Batu":
    print("Player 2 Win!\n")
    
elif player1=="B" and player2=="C" or player1=="Gunting" and player2=="Kertas":
    print("Player 1 Win!\n")

# Kertas

elif player1=="C" and player2=="C" or player1=="Kertas" and player2=="Kertas":
    print("Battle Draw!\n")
    
elif player1=="C" and player2=="A" or player1=="Kertas" and player2=="Batu":
    print("Player 1 Win!\n")
    
elif player1=="C" and player2=="B" or player1=="Kertas" and player2=="Gunting":
    print("Player 2 Win!\n")
    
else:
        print(10*"=","Ngetik yang bener WOII!!","="*10)