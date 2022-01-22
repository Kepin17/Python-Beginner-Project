# 

def tryAgain():

    print("\nPemesanan tiket di batalkan.")  
    user_choise = input(" Apakah kamu mau memesan tiket lainya? yes or no : ") 
    user_choise = user_choise.upper()

    if user_choise == "YES":
      return True
    else:
        return False  
        